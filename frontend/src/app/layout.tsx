'use client';

import { Inter } from 'next/font/google';
import { ReactNode } from 'react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import '../styles/globals.css';

// Импорт компонентов
import Header from '../components/layout/Header';
import Footer from '../components/layout/Footer';

// Инициализация шрифтов
const inter = Inter({ subsets: ['latin'] });

// Создание клиента запросов
const queryClient = new QueryClient();

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="ru">
      <head>
        <title>AI Agents Platform</title>
        <meta name="description" content="Платформа для управления ИИ-агентами" />
      </head>
      <body className={inter.className}>
        <QueryClientProvider client={queryClient}>
          <div className="flex min-h-screen flex-col">
            <Header />
            <main className="flex-1">{children}</main>
            <Footer />
          </div>
        </QueryClientProvider>
      </body>
    </html>
  );
}
