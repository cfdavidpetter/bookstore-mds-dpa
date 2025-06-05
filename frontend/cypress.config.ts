import { defineConfig } from 'cypress';

export default defineConfig({
  component: {
    devServer: {
      framework: 'next',
      bundler: 'webpack',
      webpackConfig: {
        resolve: {
          extensions: ['.js', '.jsx', '.ts', '.tsx'],
        },
      },
    },
    specPattern: 'src/shared/components/**/*.cy.{js,ts,jsx,tsx}',
    supportFile: 'cypress/support/component.ts',
    video: false,
  },
  e2e: {
    baseUrl: 'http://localhost:3000',
  },
});
