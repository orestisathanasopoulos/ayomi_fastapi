import { useState } from "react";
import { Button } from "./Button";
import "./Calculator.css";
import axios from "axios";

const Calculator = () => {
  const [operandInput, setOperandInput] = useState<string | null>("");
  const [operatorInput, setOperatorInput] = useState<string | null>("");

  const handleOperandClick = (buttonValue: string) => {
    setOperandInput(`${operandInput}${buttonValue}`);
  };

  const handleOperatorClick = (buttonValue: string) => {
    setOperatorInput(`${operatorInput} ${buttonValue}`);
    setOperandInput(`${operandInput} `);
  };

  const handClearClick = () => {
    setOperatorInput("");
    setOperandInput("");
  };

  const calculateTotal = async () => {
    try {
      const operation = JSON.stringify({
        operation: `${operandInput}${operatorInput}`,
      });
      console.log(operation);

      const response = await axios.post(
        "http://localhost:8000/calculate",
        operation,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      setOperatorInput("");
      setOperandInput(response.data.result);
    } catch (error) {
      console.log(error);
    }
  };

  const fetchData = async () => {
    try {
      const response = await axios.get("http://localhost:8000/data");
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  };

  const displayValue = `${operandInput} | ${operatorInput}`;

  return (
    <div id="calculator" className="section-bg-image">
      <div className="calculator-body">
        <div className="display">{displayValue}</div>
        <div className="buttons">
          <Button
            buttonValue="AC"
            className="button"
            onClick={() => handClearClick()}
          />
          <Button
            buttonValue="D"
            className="button"
            onClick={() => fetchData()}
          />
          <Button
            buttonValue="**"
            className="button"
            onClick={() => handleOperatorClick("**")}
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
            onClick={() => handleOperatorClick("+")}
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
            onClick={() => calculateTotal()}
          />
        </div>
      </div>
    </div>
  );
};

export default Calculator;
