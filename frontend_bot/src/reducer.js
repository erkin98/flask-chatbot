export const initialState = {
  customers: [],
  size: 10
};

export const reducer = (state, action) => {
  switch (action.type) {
    case "GET_CUSTOMERS":
      return {
        ...state,
        customers: action.customers,
      };
    case "UPDATE_SIZE":
      return {
        ...state,
        size: action.size,
      };
    default:
      return state;
  }
};
