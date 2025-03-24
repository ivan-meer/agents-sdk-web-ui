# Frontend Architecture

## Overview

The frontend of the AI Agents Platform is built using Next.js 14 and React 18, leveraging the App Router for routing and server-side rendering. It follows a component-based architecture, with a focus on modularity, reusability, and performance. 

The main goals of the frontend are:

- Provide a user-friendly interface for managing and interacting with AI agents.
- Offer a clear and intuitive way to configure agents, tools, and settings.
- Visualize agent execution and results in real-time.
- Ensure a responsive and accessible experience across different devices.

Key principles of the frontend architecture include:

- **Component-Based Architecture**: Building UI using reusable components for maintainability and scalability.
- **React Server Components**: Utilizing server components for improved performance and reduced client-side JavaScript.
- **Type Safety**: Using TypeScript for enhanced code quality and maintainability.
- **Modern UI**: Implementing a clean and modern design with Tailwind CSS and shadcn/ui components.
- **State Management**: Employing Zustand for global state management and React Context for local component state.

## Tech Stack

- **UI Framework**: [Next.js](https://nextjs.org/) 14 (App Router)
- **UI Library**: [React](https://reactjs.org/) 18
- **Styling**: [Tailwind CSS](https://tailwindcss.com/) + CSS Modules
- **Components**: [shadcn/ui](https://ui.shadcn.com/)
- **Icons**: [Lucide React](https://lucide.dev/)
- **State Management**: [Zustand](https://zustand.js.org/)
- **Data Fetching**: [TanStack Query](https://tanstack.com/query/v5/) v5
- **Form Handling**: [React Hook Form](https://react-hook-form.com/)
- **Linting**: [ESLint](https://eslint.org/)
- **Formatting**: [Prettier](https://prettier.io/)
- **Testing**: [Jest](https://jestjs.io/) + [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- **Bundler**: [Webpack](https://webpack.js.org/) (via Next.js)
- **Language**: [TypeScript](https://www.typescriptlang.org/)

## Components Structure

The frontend architecture is based on reusable and modular components. Components are organized into the following categories:

- **Layout Components**:
  - `Header`: Global header with navigation and branding.
  - `Footer`: Global footer with copyright information and links.
  - `Sidebar`: (Planned) Sidebar for navigation and settings.

- **Page Components**:
  - `Home`: Landing page with project overview and call-to-actions.
  - `Agents`: Page for managing and configuring AI agents.
  - `Tools`: Page for managing and configuring tools.
  - `Settings`: Page for user settings and preferences.
  - `Runs`: Page for viewing agent execution history and results.

- **UI Components**:
  - `Button`: Reusable button component with different styles and variants.
  - `Input`: Reusable input component for text, numbers, and other data types.
  - `Modal`: Reusable modal component for dialogs and popups.
  - `Table`: Reusable table component for displaying data in a tabular format.
  - `Card`: Reusable card component for displaying information in a container.
  - `Dropdown`: Reusable dropdown component for selecting options.
  - `Tabs`: Reusable tabs component for navigation within a page.

- **Data Components**:
  - `AgentList`: Component for displaying a list of agents.
  - `ToolList`: Component for displaying a list of tools.
  - `RunResults`: Component for displaying agent execution results.
  - `AgentForm`: Component for creating and editing agent configurations.
  - `ToolForm`: Component for creating and editing tool configurations.

This component structure provides a solid foundation for building a scalable and maintainable frontend application. As the project evolves, new components will be added and existing ones will be refined.

## State Management

State management in the frontend is handled using a combination of Zustand for global state and React Context for local component-level state.

- **Zustand**: Zustand is used for managing global application state, such as:
  - Agent configurations
  - Tool configurations
  - User settings
  - Application theme
  - Authentication status

  Zustand provides a simple and efficient way to manage global state with minimal boilerplate. Stores are defined as simple functions that return the state and actions to update the state. Components can subscribe to specific parts of the store and re-render only when those parts change.

- **React Context**: React Context is used for managing local state within component trees, such as:
  - Form state
  - UI component state (e.g., modal visibility, tab selection)
  - Theme context for components

  React Context provides a way to pass data through the component tree without having to pass props down manually at every level. It is useful for sharing state that is local to a specific part of the application.

This combination of Zustand and React Context provides a flexible and scalable approach to state management in the frontend application. Zustand is used for global, application-wide state, while React Context is used for local, component-specific state.

## Routing

The frontend uses the [Next.js App Router](https://nextjs.org/docs/app) for routing and navigation. 

Key features of the routing implementation:

- **File-System Based Routing**: Routes are defined by the directory structure in the `src/app` directory. Each folder in `app` represents a route segment, and special files like `page.tsx` and `layout.tsx` define the route handlers and layouts.
- **`page.tsx`**: A `page.tsx` file in a route segment directory makes the directory publicly accessible as a route. It defines the UI for that route.
- **`layout.tsx`**: A `layout.tsx` file defines the UI layout for a route segment and all its child routes. Layouts are used to create shared UI elements like headers and footers that persist across multiple pages.
- **Nested Routes**: Nested folders create nested routes. For example, `app/agents/create/page.tsx` creates the route `/agents/create`.
- **Dynamic Routes**: Dynamic route segments can be created using bracketed folder names, e.g., `app/agents/[agentId]/page.tsx` creates a dynamic route that matches paths like `/agents/123` or `/agents/456`.
- **Linking Between Pages**: The `Link` component from `next/link` is used for client-side navigation between pages.

Example routing structure:

```
src/app
├── layout.tsx         # Root layout
├── page.tsx           # Home page route (/)
├── agents/
│   ├── layout.tsx     # Agents layout (/agents/*)
│   ├── page.tsx       # Agents list page (/agents)
│   ├── [agentId]/     # Dynamic agent routes (/agents/[agentId])
│   │   └── page.tsx   # Agent detail page (/agents/[agentId])
│   └── create/
│       └── page.tsx   # Create agent page (/agents/create)
└── tools/
    └── page.tsx       # Tools page (/tools)
```

This file-system based routing system provides a clear and intuitive way to define and manage routes in the frontend application.

## Data Fetching

Data fetching in the frontend is primarily handled using [TanStack Query](https://tanstack.com/query/v5/). 

Key features of data fetching implementation:

- **Declarative Data Fetching**: TanStack Query allows for declarative data fetching using hooks like `useQuery` and `useMutation`. Components describe their data dependencies, and TanStack Query handles fetching, caching, and updating data.
- **Caching**: TanStack Query provides a powerful caching mechanism that reduces redundant requests and improves performance. Data is cached in the client-side cache and can be configured with different cache policies.
- **Background Updates**: TanStack Query automatically updates data in the background, ensuring that the UI is always displaying the latest information.
- **Optimistic Updates**: TanStack Query supports optimistic updates for mutations, providing a smoother user experience by updating the UI immediately and rolling back in case of errors.
- **Error Handling**: TanStack Query provides robust error handling mechanisms, allowing components to gracefully handle data fetching errors and display informative error messages.
- **Server-Side Rendering (SSR) and Server Components**: TanStack Query is designed to work seamlessly with Next.js Server Components and SSR. Queries can be pre-fetched on the server and hydrated on the client, improving initial page load performance.

Example data fetching with `useQuery`:

```typescript
import { useQuery } from '@tanstack/react-query';

function AgentList() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['agents'],
    queryFn: () => fetch('/api/agents').then(res => res.json()),
  });

  if (isLoading) return <div>Loading agents...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <ul>
      {data.map(agent => (
        <li key={agent.id}>{agent.name}</li>
      ))}
    </ul>
  );
}
```

This data fetching strategy with TanStack Query simplifies data management, improves performance, and enhances the user experience by providing efficient caching and background updates.

## Styling

Styling in the frontend is implemented using [Tailwind CSS](https://tailwindcss.com/) and CSS Modules.

- **Tailwind CSS**: Tailwind CSS is a utility-first CSS framework that provides a large set of pre-defined utility classes that can be composed to style HTML elements directly in the JSX. 
  - **Utility-First Approach**: Tailwind CSS promotes a utility-first approach, where styles are applied by composing utility classes instead of writing custom CSS. This approach leads to more maintainable and consistent styles.
  - **Customization**: Tailwind CSS is highly customizable through its configuration file (`tailwind.config.js`). The theme, colors, fonts, breakpoints, and other aspects of the styles can be customized to match the project's design requirements.
  - **Responsiveness**: Tailwind CSS provides responsive modifiers that allow applying styles conditionally based on screen sizes.

- **CSS Modules**: CSS Modules are used for component-level styling and for styling parts of the application where Tailwind CSS utilities are not sufficient.
  - **Component Scoping**: CSS Modules automatically scope CSS class names to the component in which they are imported. This prevents class name collisions and ensures that styles are encapsulated within components.
  - **Local Styles**: CSS Modules are ideal for styling complex components or for adding custom styles that are specific to a component.

- **`globals.css`**: The `frontend/src/styles/globals.css` file is used to define global styles, such as:
  - Base styles for HTML elements
  - Global CSS variables (custom properties)
  - Tailwind CSS directives (`@tailwind base`, `@tailwind components`, `@tailwind utilities`)

This styling strategy combines the benefits of utility-first styling with Tailwind CSS and component-level styling with CSS Modules, providing a flexible and maintainable approach to styling the frontend application.

## Testing

Testing in the frontend is implemented using [Jest](https://jestjs.io/) as the test runner and [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/) for component testing.

- **Jest**: Jest is a JavaScript test runner that provides a complete testing solution with features like:
  - Test runner and assertion library
  - Mocking and spying capabilities
  - Code coverage reporting
  - Parallel test execution
  - Watch mode for rapid feedback during development

- **React Testing Library**: React Testing Library is a testing utility that focuses on testing components from the user's perspective. 
  - **User-Centric Testing**: React Testing Library encourages testing components by interacting with them as a user would, rather than testing implementation details.
  - **DOM Queries**: React Testing Library provides utilities for querying the DOM in a way that reflects how users interact with the UI (e.g., `getByRole`, `getByLabelText`, `getByText`).
  - **Accessibility**: React Testing Library promotes accessibility by encouraging tests that interact with components in an accessible way.

- **Types of Tests**: The frontend testing strategy includes:
  - **Unit Tests**: Testing individual components in isolation to ensure they function correctly.
  - **Integration Tests**: Testing the interactions between components and modules to ensure they work together as expected.
  - **End-to-End (E2E) Tests**: (Planned) E2E tests using Playwright or Cypress to test the entire application flow from the user's perspective.

Example unit test using React Testing Library and Jest:

```typescript
import { render, screen } from '@testing-library/react';
import { Button } from '../components/Button';

describe('Button', () => {
  it('renders button with text', () => {
    render(<Button>Click me</Button>);
    const buttonElement = screen.getByRole('button', { name: /click me/i });
    expect(buttonElement).toBeInTheDocument();
  });
});
```

This testing strategy ensures the quality and reliability of the frontend application by providing comprehensive coverage at different levels of the component hierarchy.

## Deployment

The frontend application is designed to be easily deployed to platforms like [Vercel](https://vercel.com/), [Netlify](https://www.netlify.com/), or [AWS](https://aws.amazon.com/). 

**Deployment to Vercel (Recommended)**

[Vercel](https://vercel.com/) is the recommended platform for deploying Next.js applications due to its seamless integration and optimized performance.

Steps to deploy to Vercel:

1. **Create a Vercel account**: Sign up for a Vercel account at [https://vercel.com/](https://vercel.com/).
2. **Install Vercel CLI**: Install the Vercel CLI globally using npm or yarn:
   ```bash
   npm install -g vercel
   ```
3. **Deploy from CLI**: Navigate to the frontend project directory in your terminal and run:
   ```bash
   vercel
   ```
4. **Follow Vercel CLI prompts**: The Vercel CLI will guide you through the deployment process, including linking your project to your Vercel account and configuring deployment settings.
5. **Automatic deployments**: Once the project is set up on Vercel, any changes pushed to the connected Git repository (e.g., GitHub, GitLab, Bitbucket) will automatically trigger a new deployment.

**Alternative Deployment Options**

- **Netlify**: [Netlify](https://www.netlify.com/) is another popular platform for deploying frontend applications. Deployment to Netlify is similar to Vercel and can be done via Netlify CLI or Git integration.
- **AWS**: [AWS](https://aws.amazon.com/) provides various services for deploying frontend applications, such as AWS S3 for static hosting and AWS CloudFront for CDN. Deployment to AWS requires more manual configuration but offers greater flexibility and control.

For production deployments, it is recommended to use a platform like Vercel or Netlify for ease of use and optimized performance. For more complex deployments or specific AWS infrastructure requirements, AWS services can be used.

Ensure that environment variables are configured correctly for the chosen deployment platform, especially API endpoints and any API keys required for the frontend application to communicate with the backend.
