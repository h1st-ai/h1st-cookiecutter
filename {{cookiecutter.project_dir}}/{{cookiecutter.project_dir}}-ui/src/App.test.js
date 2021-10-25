import { render, screen } from '@testing-library/react';
import App from './App';

test('renders translate page', () => {
  render(<App />);
  const linkElement = screen.getByText(/language translator/i);
  expect(linkElement).toBeInTheDocument();
});
