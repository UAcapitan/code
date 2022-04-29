import React from "react";

export default function ToDoList(props) {
    return(
        <ul>
            { props.todos.map(todo => {
                return <li key={todo.id}>{todo.id}. {todo.text}</li>
            })}
        </ul>
    )
}