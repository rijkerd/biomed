import React, { useReducer, useContext, createContext } from "react";

export const StateContext = createContext();

console.log(StateContext);

export const StateProvider = ({ reducer, initialState, children }) => (
  <StateContext.Provider value={useReducer(reducer, initialState)}>
    {children}
  </StateContext.Provider>
);

export const useStateValue = () => useContext(StateContext);

const App = () => <h1>Hello world</h1>;

export default App;
