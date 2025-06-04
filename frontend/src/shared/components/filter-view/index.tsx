import { useState, useEffect } from "react";
import { Input } from "../ui/input";
import { Button } from "../ui/button";
import { FilterInput } from "./types";

function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState<T>(value);

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(timer);
    };
  }, [value, delay]);

  return debouncedValue;
}

export default function FilterView({
  inputsData,
  setFilters,
  resetFilters,
}: {
  inputsData: FilterInput[];
  setFilters: (filters: string) => void;
  resetFilters: () => void;
}) {

  const [inputs, setInputs] = useState<FilterInput[]>(inputsData);
  const debouncedInputs = useDebounce(inputs, 500);

  useEffect(() => {
    const filterString = debouncedInputs
      .filter(input => input.value)
      .map(input => `${input.column}:${input.value}`)
      .join(';');

    setFilters(filterString);
  }, [debouncedInputs, setFilters]);

  const handleReset = () => {
    setInputs(inputs.map((input) => ({ ...input, value: "" })));
    resetFilters();
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
        <Button
          variant="outline"
          className="w-full md:w-1/4"
          onClick={handleReset}
        >
          Reset
        </Button>
      </div>
    </div>
  );
}
