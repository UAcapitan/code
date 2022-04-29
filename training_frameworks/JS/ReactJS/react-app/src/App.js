import React from "react";
import ToDoList from "./ToDo/ToDoList";

function App() {
  const todos = [
    {id: 1, completed: false, text: 'Buy milk'},
    {id: 2, completed: false, text: 'Do homework'},
    {id: 3, completed: false, text: 'Take a shower'},
  ]

  return (
    <div className="wrapper">
      <h1>Tutorial</h1>
      <br />
      <p>Hello, world!</p>
      <ToDoList todos={todos} />
    </div>
  );
}

export default App;
