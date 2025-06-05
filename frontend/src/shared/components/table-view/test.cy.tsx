import TableView from "./index";

describe("TableView", () => {

  interface MockT {
    id: number;
    name: string;
    email: string;
  }

  const data = [
    {
      id: 1,
      name: "John Doe",
      email: "john@example.com",
    },
    {
      id: 2,
      name: "Jane Doe 2",
      email: "jane_2@example.com",
    },
    {
      id: 3,
      name: "John Smith",
      email: "john@example.com",
    },
  ];

  const columns = [
    { header: "Name", accessor: "name" as keyof MockT },
    { header: "Email", accessor: "email" as keyof MockT },
  ]


  beforeEach(() => {
    cy.mount(
      <TableView data={data} columns={columns} actions={[]} />
    );
  });

  it("should render the component", () => {
    cy.get("table th").should("contain", "Name").should("contain", "Email");
    cy.get("table td").should("contain", "John Doe").should("contain", "john@example.com");
    cy.get("table td").should("contain", "Jane Doe 2").should("contain", "jane_2@example.com");
    cy.get("table td").should("contain", "John Smith").should("contain", "john@example.com");
  });
});
