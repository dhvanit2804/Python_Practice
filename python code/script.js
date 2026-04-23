const express = required("express");
const app = express();

app.get("/users", (req, res) => {
  const users = [{ id: 1, name: "Dhvanit" }];
  res.json(users);
});

app.listen(3000, () => {
  console.log("The app running");
});

fetch("https://jsonplaceholder.typicode.com/users")
  .then((res) => {
    res.json();
  })
  .then((data) => {
    console.log(data);
  })
  .catch((err) => {
    console.log(err);
  });

async function getUser() {
  try {
    let res = await fetch("https://jsonplaceholder.typicode.com/users");
    let data = await res.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}
