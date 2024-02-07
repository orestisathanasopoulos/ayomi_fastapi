import React, { useState } from "react";
import { Button } from "./Button";
import "./Calculator.css";

const Calculator = () => {
  const [operandInput, setOperandInput] = useState("");
  const [operatorInput, setOperatorInput] = useState("");

  const handleOperandClick = (buttonValue: string) => {
    setOperandInput(`${operandInput} ${buttonValue}`);
  };

  const handleOperatorClick = (buttonValue: string) => {
    setOperatorInput(`${operatorInput} ${buttonValue}`);
  };

  const displayValue = "0";

  return (
    <div id="calculator" className="section-bg-image">
      <h2>Lets do some math!</h2>
      <div className="calculator-body">
        <div className="display">{displayValue}</div>
        <div className="buttons">
          <Button
            buttonValue="AC"
            className="button"
            onClick={() => handleButtonClick("AC")}
          />
          <Button
            buttonValue="-"
            className="button"
            onClick={() => handleOperatorClick("-")}
          />
          <Button
            buttonValue="-"
            className="button"
            onClick={() => handleOperatorClick("-")}
          />
          <Button
            buttonValue="÷"
            className="button right-button"
            onClick={() => handleOperatorClick("÷")}
          />
        </div>

        <div className="buttons">
          <Button
            buttonValue="7"
            className="button"
            onClick={() => handleOperandClick("7")}
          />
          <Button
            buttonValue="8"
            className="button"
            onClick={() => handleOperandClick("8")}
          />
          <Button
            buttonValue="9"
            className="button"
            onClick={() => handleOperandClick("9")}
          />
          <Button
            buttonValue="*"
            className="button right-button"
            onClick={() => handleOperatorClick("*")}
          />
        </div>
        <div className="buttons">
          <Button
            buttonValue="4"
            className="button"
            onClick={() => handleOperandClick("4")}
          />
          <Button
            buttonValue="5"
            className="button"
            onClick={() => handleOperandClick("5")}
          />
          <Button
            buttonValue="6"
            className="button"
            onClick={() => handleOperandClick("6")}
          />
          <Button
            buttonValue="-"
            className="button right-button"
            onClick={() => handleOperatorClick("-")}
          />
        </div>
        <div className="buttons">
          <Button
            buttonValue="1"
            className="button"
            onClick={() => handleOperandClick("1")}
          />
          <Button
            buttonValue="2"
            className="button"
            onClick={() => handleOperandClick("2")}
          />
          <Button
            buttonValue="3"
            className="button"
            onClick={() => handleOperandClick("3")}
          />
          <Button
            buttonValue="+"
            className="button right-button"
            onClick={() => handleOperandClick("+")}
          />
        </div>
        <div className="buttons">
          <Button
            buttonValue="0"
            className="button zero-button"
            onClick={() => handleOperandClick("0")}
          />
          <Button
            buttonValue="."
            className="button"
            onClick={() => handleOperandClick(".")}
          />
          <Button
            buttonValue="="
            className="button right-button"
            onClick={() => handleButtonClick("=")}
          />
        </div>
      </div>
    </div>
  );
};

export default Calculator;
