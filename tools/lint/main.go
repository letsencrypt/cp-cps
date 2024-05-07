package main

import (
	"bufio"
	_ "embed"
	"fmt"
	"os"
	"slices"
	"strings"
)

//go:embed outline.txt
var outline string

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "must provide path to document to check")
		os.Exit(1)
	}

	file, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Fprintln(os.Stderr, "opening document:", err)
		os.Exit(1)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading document:", err)
		os.Exit(1)
	}

	anyErr := false

	errs := make(chan error)
	go func() {
		lintHeadings(lines, errs)
		close(errs)
	}()
	for err = range errs {
		anyErr = true
		fmt.Fprintln(os.Stderr, err)
	}

	errs = make(chan error)
	go func() {
		lintEmptySections(lines, errs)
		close(errs)
	}()
	for err = range errs {
		anyErr = true
		fmt.Fprintln(os.Stderr, err)
	}

	if anyErr {
		os.Exit(1)
	}

	fmt.Println("lint checks complete; no findings")
}

// lintHeadings tries to locate every heading that we expect to exist, and
// checks that they appear in the correct order.
func lintHeadings(lines []string, errs chan<- error) {
	outline = strings.TrimSpace(outline)
	headings := strings.Split(outline, "\n")
	headingLines := make([]int, len(headings))

	for i, heading := range headings {
		headingLines[i] = slices.Index(lines, heading)
	}

	for i, lineNo := range headingLines {
		if lineNo == -1 {
			errs <- fmt.Errorf("heading %q not found", headings[i])
			continue
		}

		if i > 0 && lineNo <= headingLines[i-1] {
			errs <- fmt.Errorf("heading %q found out-of-order on line %d", headings[i], lineNo)
			continue
		}
	}
}

// lintEmptySections looks for places where two section headings occur with
// nothing other than empty lines between them, and the second section is of
// equal or lesser depth (being of greater depth is fine, that's a subsection).
func lintEmptySections(lines []string, errs chan<- error) {
	lastHeadingDepth := 0
	sectionBodySeen := false
	for i, line := range lines {
		if line == "" {
			continue
		}

		if strings.HasPrefix(line, "#") {
			currHeadingDepth := len(line) - len(strings.TrimLeft(line, "#"))
			if currHeadingDepth <= lastHeadingDepth && !sectionBodySeen {
				errs <- fmt.Errorf("empty section found at line %d", i)
			}

			lastHeadingDepth = currHeadingDepth
			sectionBodySeen = false
			continue
		}

		sectionBodySeen = true
	}
}
