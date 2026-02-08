## Folder Structure

```
**Option 1: Flat Structure (Small to Medium Libraries)**

src/
├── components/
│ ├── Button/
│ │ ├── Button.tsx
│ │ ├── Button.module.css
│ │ ├── Button.test.tsx
│ │ ├── Button.stories.tsx
│ │ └── index.ts
│ ├── Input/
│ │ ├── Input.tsx
│ │ ├── Input.module.css
│ │ └── index.ts
│ └── index.ts // Exports all components
├── tokens/
│ ├── colors.ts
│ ├── spacing.ts
│ ├── typography.ts
│ └── index.ts
├── utils/
│ └── classNames.ts
└── types/
└── common.ts

**Option 2: Grouped Structure (Large Libraries)**


src/
├── components/
│ ├── base/ // Primitives
│ │ ├── Button/
│ │ ├── Input/
│ │ └── Icon/
│ ├── form/ // Form-specific
│ │ ├── TextField/
│ │ ├── Select/
│ │ └── Checkbox/
│ ├── data-display/ // Tables, charts
│ │ ├── DataGrid/
│ │ ├── TelemetryChart/
│ │ └── MetricCard/
│ ├── feedback/ // Alerts, modals
│ │ ├── Alert/
│ │ ├── Modal/
│ │ └── Toast/
│ └── layout/ // Containers, grids
│ ├── Container/
│ ├── Grid/
│ └── Stack/
├── hooks/
│ ├── useDebounce.ts
│ └── useKeyPress.ts
├── tokens/   // these get passed into a theme provider
│ ├── colors.ts
│ ├── spacing.ts
│ └── typography.ts
└── utils/
```

## Component Patterns

### Basic

```tsx
// Button.tsx
import React from "react";
import styles from "./Button.module.css";
import { classNames } from "@/utils";

// Define as const enums or string literals (store in a types file if they are reusable)
type ButtonVariant = "primary" | "secondary" | "tertiary" | "danger";
type ButtonSize = "small" | "medium" | "large";
type AlertSeverity = "info" | "warning" | "error" | "success";

/**
 * Primary button component for user actions.
 *
 * @example
 * <Button variant="primary" onClick={handleSubmit}>
 *   Submit
 * </Button>
 */
// Extend native HTML props - extends React.ButtonHTMLAttributes gives you all standard button props
export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  // Explicit default params - easier to understand than implicit behavior
  /**
   * Visual style variant
   * @default 'primary'
   */
  variant?: ButtonVariant;
  size?: ButtonSize;

  // boolean prefix: is/has/should
  isLoading?: boolean;
  isDisabled?: boolean;
  startIcon?: React.ReactNode;
  endIcon?: React.ReactNode;
  /**
   * @deprecated Use `size=...` instead. Will be removed in v3.0.0
   */
  isFullWidth?: boolean;

  // accessibility: aria prefix
  ariaLabel?: string;
  "Submit form";
}

// Use forwardRef - allows parent components to access the DOM element
export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      variant = "primary",
      size = "medium",
      isLoading = false,
      isDisabled = false,
      startIcon,
      endIcon,
      isFullWidth = false,
      children,
      className,
      ...restProps
    },
    ref,
  ) => {
    const buttonClasses = classNames(
      styles.button,
      styles[variant],
      styles[size],
      isFullWidth && styles.fullWidth,
      isLoading && styles.loading,
      // className merging - allow consumers to add custom classes without breaking your styles
      className,
    );

    return (
      <button
        ref={ref}
        className={buttonClasses}
        disabled={isDisabled || isLoading}
        {...restProps}
      >
        {isLoading && <Spinner size="small" />}
        {!isLoading && startIcon && (
          <span className={styles.startIcon}>{startIcon}</span>
        )}
        <span className={styles.content}>{children}</span>
        {!isLoading && endIcon && (
          <span className={styles.endIcon}>{endIcon}</span>
        )}
      </button>
    );
  },
);

Button.displayName = "Button";
```

### Composition

```tsx
// TelemetryPanel.tsx
export const TelemetryPanel = ({ children }: { children: React.ReactNode }) => {
  return <div className={styles.panel}>{children}</div>;
};

TelemetryPanel.Header = ({ children }: { children: React.ReactNode }) => {
  return <div className={styles.header}>{children}</div>;
};

TelemetryPanel.Body = ({ children }: { children: React.ReactNode }) => {
  return <div className={styles.body}>{children}</div>;
};

TelemetryPanel.Footer = ({ children }: { children: React.ReactNode }) => {
  return <div className={styles.footer}>{children}</div>;
};

// Usage - very flexible
<TelemetryPanel>
  <TelemetryPanel.Header>
    <h2>Engine Status</h2>
  </TelemetryPanel.Header>
  <TelemetryPanel.Body>
    <MetricDisplay label="Temperature" value={temp} />
  </TelemetryPanel.Body>
  <TelemetryPanel.Footer>Last updated: {timestamp}</TelemetryPanel.Footer>
</TelemetryPanel>;
```

### Render Props

```tsx
interface DataFetcherProps<T> {
  url: string;
  children: (
    data: T | null,
    isLoading: boolean,
    error: Error | null,
  ) => React.ReactNode;
}

function DataFetcher<T>({ url, children }: DataFetcherProps<T>) {
  const [data, setData] = useState<T | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  // fetch logic...

  return <>{children(data, isLoading, error)}</>;
}

// Usage
<DataFetcher<TelemetryData> url="/api/telemetry">
  {(data, isLoading, error) => {
    if (isLoading) return <Spinner />;
    if (error) return <Alert severity="error">{error.message}</Alert>;
    return <TelemetryDisplay data={data} />;
  }}
</DataFetcher>;
```

### Slot

```tsx
interface CardProps {
  header?: React.ReactNode;
  content: React.ReactNode;
  actions?: React.ReactNode;
  footer?: React.ReactNode;
}

const Card = ({ header, content, footer, actions }: CardProps) => (
  <div className={styles.card}>
    {header && <div className={styles.header}>{header}</div>}
    <div className={styles.content}>{content}</div>
    {actions && <div className={styles.actions}>{actions}</div>}
    {footer && <div className={styles.footer}>{footer}</div>}
  </div>
);
```

### ClassName API

```tsx
interface ButtonProps {
  /** Custom class for root element */
  className?: string;

  /** Classes for specific parts */
  classes?: {
    root?: string;
    startIcon?: string;
    endIcon?: string;
  };
}

// Allows precise styling control
<Button
  className="my-custom-button"
  classes={{
    startIcon: "my-icon-styles",
  }}
/>;
```
