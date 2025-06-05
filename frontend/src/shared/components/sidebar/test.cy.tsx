import Sidebar from "./index";

describe("Sidebar", () => {

  const MockIcon = () => <div>MockIcon</div>;

  const routes = [
    {
      href: "/books",
      icon: MockIcon as React.ElementType,
      label: "Books",
    },
    {
      href: "/authors",
      icon: MockIcon as React.ElementType,
      label: "Authors",
    },
  ];

  beforeEach(() => {
    cy.mount(
      <Sidebar routes={routes} />
    );
  });

  it("should render the component", () => {
    cy.get("nav").should("contain", "Books");
    cy.get("nav").should("contain", "Authors");
  });
});
