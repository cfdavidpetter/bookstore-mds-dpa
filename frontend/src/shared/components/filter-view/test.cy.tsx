import FilterView from "./index";
import { FilterInput } from "./types";

describe("FilterView", () => {
  const mockInputsData: FilterInput[] = [
    {
      label: "Name",
      column: "name",
      type: "text",
      placeholder: "Search by name",
      value: "",
    },
    {
      label: "Email",
      column: "email",
      type: "email",
      placeholder: "Search by email",
      value: "",
    },
  ];

  let mockSetFilters;
  let mockResetFilters;

  beforeEach(() => {
    mockSetFilters = cy.stub().as("setFilters");
    mockResetFilters = cy.stub().as("resetFilters");

    cy.mount(
      <FilterView
        inputsData={mockInputsData}
        setFilters={mockSetFilters}
        resetFilters={mockResetFilters}
      />
    );
  });

  it("renders the component", () => {
    cy.get("h2").should("contain", "Filters");
    cy.get("input[name='name']").should("have.length", 1);
    cy.get("input[name='email']").should("have.length", 1);
    cy.get("button[name='reset-filters']").should("contain", "Reset");
  });

  it("should set filters when inputs change", () => {
    cy.get("input[name='name']").type("John");
    cy.get("input[name='email']").type("john@example.com");
    cy.get("@setFilters").should(
      "have.been.calledWith",
      "name:John;email:john@example.com"
    );
  });

  it("should reset filters when reset button is clicked", () => {
    cy.get("input[name='name']").type("John");
    cy.get("input[name='email']").type("john@example.com");

    cy.get("input[name='name']").should("have.value", "John");
    cy.get("input[name='email']").should("have.value", "john@example.com");

    cy.get("button[name='reset-filters']").click();
    cy.get("@resetFilters").should("have.been.called");

    cy.get("input[name='name']").should("have.value", "");
    cy.get("input[name='email']").should("have.value", "");
  });

  it("should handle empty input values", () => {
    cy.get("input[name='name']").type("John").clear();
    cy.get("input[name='email']").type("john@example.com").clear();
    cy.get("@setFilters").should("have.been.calledWith", "");
  });

  it("should handle single filter input", () => {
    cy.get("input[name='name']").type("John");
    cy.get("@setFilters").should("have.been.calledWith", "name:John");
  });

  it("should handle special characters in input", () => {
    cy.get("input[name='name']").type("John Doe");
    cy.get("input[name='email']").type("john.doe@example.com");
    cy.get("@setFilters").should(
      "have.been.calledWith",
      "name:John Doe;email:john.doe@example.com"
    );
  });
});
