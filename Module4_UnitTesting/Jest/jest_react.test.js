import React from 'react';
import {render,screen,fireEvent} from '@testing-library/react';

const MyButton=()=><button onClick={
    ()=>alert('Hi')}>Click Me</button>;

test('renders button and clicks it', ()=>{
  render(<MyButton />);
  const button=screen.getByText('Click Me');
  expect(button).toBeInTheDocument();
  fireEvent.click(button);
});