## CSS

[CSS study guide](https://www.freecodecamp.org/learn/responsive-web-design-v9/review-css/review-css)

## Heuristics (Nielsen's 10 Usability Heuristics)

Guidelines to make user interface more usable/friendly/intuitve

1. Visibility of System Status: keep indicators/statuses/progress-bars visible, show confirmation messages after actions
2. Match Between System and the Real World: use language the operator uses
3. User Control and Freedom: be able to exit something, cancel/abort, undo/redo
4. Consistency and Standards
5. Error Prevention: alert/warn users about the implications of starting/stop/exiting can do to the system
6. Recognition Rather Than Recall: make it easy for users to find things rather than having to remember where something is at
7. Flexibility and Efficiency of Use: make system flexible for new and advanced users. Advanced users can do keyboard shortcuts or custom layouts
8. Aesthetic and Minimalist Design
9. Help Users Recognize, Diagnose, and Recover from Errors
10. Help and Documentation

### Other Guidelines

### Feedback Loops

Every user action needs a reaction. Immediate (button press), intermediate (loading state), and completion (success/error). In React, this means managing loading states, optimistic updates, and error boundaries properly.

### Progressive Disclosure

Show users only what they need right now, reveal complexity as needed. Good for dashboard design - summary → details → deep diagnostics. Implement with collapsible panels, tabs, modals, or drill-down navigation.

### Information Scent

Users follow "clues" that they're on the right path to their goal. Labels, breadcrumbs, and navigation hints should make it obvious where to go. Weak scent = users get lost.

## User Research Basics

- Contextual inquiry - watch them use it without interrupting them
- User interviews - Tell them "show me how you handle/do X"
- Jobs to be Done - Focus on what they are trying to accomplish; not what features they want
- Assumption Testing - Assume they need something and test it out with them and see if you get the epected outcome from the user

## Information Architecture

How to organize content:
Card sorting - have users group features/data into categories that make sense to them
Site maps & navigation hierarchies - plan structure before building
Labeling - use terminology your users already use

## Visual Hierarchy

- Size: bigger → more important. for blogs and articles, there should only be 1 h1 at the top, the following should be h2s and everything related to h2s should be h3s and so on
- Color:
  - 60-30-10 rule - dominant color 60%, secondary 30%, accent 10%
  - Contrast - WCAG requires 4.5:1 for text, 3:1 for UI elements
  - Color blindness - never use color alone (add icons, labels, patterns)
  - Semantic colors - red = danger/stop, green = success/go, yellow = warning (but culturally dependent)
- Position: top-left is typically scanned first (western users)
- White space - isolation makes things stand up or group things together
- Typeography (weight and style indicate importance):
  - Size, weight, and color to distinguish heading levels
  - Type scale - establish consistent sizes (headings, body, captions)
  - Line height - 1.5x for body text, tighter for headings
  - Line length - 50-75 characters for readability
- Layout & Spacing:
  - Grid systems - 8pt or 4pt grid for consistency
  - Spacing scale - 4, 8, 16, 24, 32, 64px (powers of 2 or fibonacci)
  - Alignment - everything should line up with something
  - Proximity - related items closer together, unrelated items farther apart

## Accessibility (A11y) Essentials

### Keyboard Navigation

- All interactive elements accessible via Tab
- Logical tab order (matches visual flow)
- Focus indicators visible
- Escape closes modals/menus

### Screen Readers

- Semantic HTML (button, nav, main, header)
- ARIA labels when semantics aren't enough
- Alt text for images (empty alt="" for decorative)
- Announce dynamic changes (aria-live regions)

### WCAG Guidelines (Web Content Accessibility Guidelines)

- Level A - basic (minimum)
- Level AA - standard target for most orgs
- Level AAA - enhanced (not always achievable)

### Key AA requirements

- 4.5:1 contrast for normal text
- 3:1 for large text and UI components
- No content that flashes more than 3 times per second
- Keyboard accessible
- Meaningful link text (not "click here")
