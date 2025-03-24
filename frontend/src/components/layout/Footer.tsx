'use client';

import Link from 'next/link';

const Footer = () => {
  return (
    <footer className="w-full border-t border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900">
      <div className="container mx-auto px-4 py-6 md:py-8">
        <div className="grid grid-cols-1 gap-8 md:grid-cols-3">
          {/* Column 1 */}
          <div>
            <h2 className="mb-4 text-lg font-semibold text-gray-900 dark:text-white">AI Agents Platform</h2>
            <p className="text-sm text-gray-600 dark:text-gray-300">
              Универсальная платформа для создания, настройки и запуска интеллектуальных агентов
            </p>
          </div>

          {/* Column 2 */}
          <div>
            <h3 className="mb-4 text-sm font-semibold uppercase text-gray-900 dark:text-white">Ресурсы</h3>
            <ul className="space-y-2 text-sm text-gray-600 dark:text-gray-300">
              <li>
                <Link href="/docs" className="hover:text-primary-600 dark:hover:text-primary-500">
                  Документация
                </Link>
              </li>
              <li>
                <Link href="/examples" className="hover:text-primary-600 dark:hover:text-primary-500">
                  Примеры
                </Link>
              </li>
              <li>
                <Link href="/blog" className="hover:text-primary-600 dark:hover:text-primary-500">
                  Блог
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 3 */}
          <div>
            <h3 className="mb-4 text-sm font-semibold uppercase text-gray-900 dark:text-white">Связь</h3>
            <ul className="space-y-2 text-sm text-gray-600 dark:text-gray-300">
              <li>
                <Link href="/contact" className="hover:text-primary-600 dark:hover:text-primary-500">
                  Контакты
                </Link>
              </li>
              <li>
                <a
                  href="https://github.com/your-username/ai-agents-platform"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="hover:text-primary-600 dark:hover:text-primary-500"
                >
                  GitHub
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-8 border-t border-gray-200 dark:border-gray-800 pt-6 text-center text-sm text-gray-600 dark:text-gray-300">
          <p>&copy; {new Date().getFullYear()} AI Agents Platform. Все права защищены.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
