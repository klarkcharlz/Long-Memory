import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import * as Sentry from "@sentry/react";
import { BrowserTracing } from "@sentry/tracing";
import {UserProvider} from "./components/UserProvider/UserProvider";
import { SENTRY_DSN } from './functions/api_constants';


// Sentry.init({
//   dsn: SENTRY_DSN,
//   integrations: [new BrowserTracing()],
//   tracesSampleRate: 1.0,
// });

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <UserProvider>
        <App/>
    </UserProvider>
);
