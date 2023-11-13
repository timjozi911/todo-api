<div id="header" align="center">
  <img src="https://media.giphy.com/media/3oKHWtXlzTHeuVewtq/giphy.gif"/>
  <p> This is an API project for Todo's that I will use for some front-end projects that I will be working on. </p>
  <p> Using this project to learn how to use FastAPI </p>
</div>

## API Reference

#### Get all todos

```http
  GET /api/todos
```

#### Get a todo

```http
  GET /api/todos/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |
