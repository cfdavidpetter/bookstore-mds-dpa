import PaginationView from "./index";
import { PaginatedResponse } from "./types";

describe("PaginationView", () => {
  interface MockT {
    id: number;
    name: string;
    email: string;
  }

  const mockT: MockT[] = [
    {
      id: 1,
      name: "John Doe",
      email: "john@example.com",
    },
    {
      id: 2,
      name: "Jane Doe",
      email: "jane@example.com",
    },
    {
      id: 3,
      name: "John Smith",
      email: "john@example.com",
    },
  ];

  const mockPaginatedResponse: PaginatedResponse<MockT> = {
    data: mockT,
    total: mockT.length,
    per_page: 10,
    from: 0,
    current_page: 1,
    next_page: 2,
    previous_page: 0,
    last_page: 1,
  };

  const mockPaginatedResponseWithMoreThan100Items: PaginatedResponse<MockT> = {
    ...mockPaginatedResponse,
    total: 100,
    last_page: 10,
    next_page: 2,
    previous_page: 0
  };

  let mockFetchItems: (page: number, filters?: string) => void;
  let filters = "";

  beforeEach(() => {
    mockFetchItems = cy.stub().as("fetchItems");
    cy.mount(
      <div className="mt-4">
        {PaginationView<MockT>(mockPaginatedResponse, mockFetchItems, filters)}
      </div>
    );
  });

  it("should render the component", () => {
    cy.get("div").should("exist");
    cy.get("div").should("contain", "1");
  });

  it("should not have a previous page button if the current page is 1", () => {
    cy.get("a[title='previous-page']").should("not.exist");
    cy.get("a[title='next-page']").should("not.exist");
  });

  it("should fetch items when the next page button is clicked", () => {
    filters = "name:John";

    mockFetchItems = cy.stub().as("fetchItems");
    cy.mount(
      <div className="mt-4">
        {PaginationView<MockT>(mockPaginatedResponseWithMoreThan100Items, mockFetchItems, filters)}
      </div>
    );

    cy.get("a[title='next-page']").click();
    cy.wait(1000);
    cy.get("@fetchItems").should("have.been.called");
  });

  it("There should be a next button as we have more than 100 items and 10 per page.", () => {
    cy.mount(
      <div className="mt-4">
        {PaginationView<MockT>(mockPaginatedResponseWithMoreThan100Items, mockFetchItems, filters)}
      </div>
    );

    cy.get("a[title='previous-page']").should("not.exist");
    cy.get("a[title='next-page']").should("exist");
  });

  it("There should be a next button as we have more than 100 items and 10 per page.", () => {
    mockPaginatedResponse.total = 100;
    mockPaginatedResponse.current_page = 8;
    mockPaginatedResponse.from = 7;
    mockPaginatedResponse.next_page = 9;
    mockPaginatedResponse.previous_page = 7;
    mockPaginatedResponse.last_page = 10;

    cy.mount(
      <div className="mt-4">
        {PaginationView<MockT>(mockPaginatedResponse, mockFetchItems, filters)}
      </div>
    );

    cy.get("a[title='previous-page']").should("exist");
    cy.get("a").should("contain", "7");
    cy.get("a").should("contain", "8");
    cy.get("a").should("contain", "9");
    cy.get("a[title='next-page']").should("exist");
  });
});
