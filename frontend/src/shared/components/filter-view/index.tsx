import { Input } from "../ui/input";
import { Button } from "../ui/button";
import { useState } from "react";

export default function FilterView() {
  const [inputs, setInputs] = useState([
    {
      label: "Search",
      type: "text",
      placeholder: "Search",
      value: "",
    },
    {
      label: "Author",
      type: "text",
      placeholder: "Author",
      value: "",
    },
    {
      label: "Publisher",
      type: "text",
      placeholder: "Publisher",
      value: "",
    },
  ]);

  const handleReset = () => {
    setInputs(inputs.map(input => ({ ...input, value: "" })));
  };

  const handleInputChange = (index: number, value: string) => {
    const newInputs = [...inputs];
    newInputs[index] = { ...newInputs[index], value };
    setInputs(newInputs);
  };

  return (
    <div className="flex flex-col items-start md:items-center gap-2 mb-4">
      <h2 className="text-lg">Filters</h2>
      <div className="flex flex-col w-full md:w-1/2 md:flex-row items-center gap-2">
        {inputs.map((input, index) => (
          <Input
            key={input.label}
            type={input.type}
            placeholder={input.placeholder}
            value={input.value}
            onChange={(e) => handleInputChange(index, e.target.value)}
            className="w-full md:w-1/2"
          />
        ))}
        <Button variant="outline" className="w-full md:w-1/4" onClick={handleReset}>
          Reset
        </Button>
      </div>
    </div>
  );
}
