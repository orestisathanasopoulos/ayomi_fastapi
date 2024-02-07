import React from "react";

interface ButtonProps {
  buttonValue: string;
  onClick: React.MouseEventHandler<HTMLButtonElement>;
  className: string;
}

export const Button = ({ buttonValue, className, onClick }: ButtonProps) => (
  <button type="button" className={className} onClick={onClick}>
    {buttonValue}
  </button>
);
