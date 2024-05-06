package main

import (
	"bufio"
	_ "embed"
	"errors"
	"fmt"
	"os"
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

	err = lintHeadings(lines)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		anyErr = true
	}

	err = lintEmptySections(lines)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		anyErr = true
	}

	if anyErr {
		os.Exit(1)
	}

}

func lintHeadings(lines []string) error {
	headings := strings.Split(outline, "\n")

	nextHeadIdx := 0
	for _, line := range lines {
		if line == headings[nextHeadIdx] {
			// If we found the heading we're looking for, start searching for the
			// next one.
			nextHeadIdx++
		}

		if nextHeadIdx == len(headings) {
			// If we've found all the headings we expect, we're done.
			break
		}
	}

	if nextHeadIdx != len(headings) {
		return fmt.Errorf("expected heading %q not found", headings[nextHeadIdx])
	}
	return nil
}

func lintEmptySections(lines []string) error {
	lastHeadingDepth := 0
	sectionBodySeen := false
	for _, line := range lines {
		if line == "" {
			continue
		}

		if strings.HasPrefix(line, "#") {
			currHeadingDepth := len(line) - len(strings.TrimLeft(line, "#"))
			if currHeadingDepth <= lastHeadingDepth && !sectionBodySeen {
				return errors.New("empty section found")
			}

			lastHeadingDepth = currHeadingDepth
			sectionBodySeen = false
			continue
		}

		sectionBodySeen = true
	}

	return nil
}
