<!-- todo.html -->
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Tiny Todo</title>
  <style>
    body{font-family:sans-serif;max-width:600px;margin:2rem auto}
    li.done{text-decoration:line-through;color:gray}
  </style>
</head>
<body>
  <h1>Tiny Todo</h1>
  <input id="new" placeholder="Add todo..." />
  <button id="add">Add</button>
  <ul id="list"></ul>

  <script>
    const listEl = document.getElementById('list');
    const newEl = document.getElementById('new');
    const KEY = 'tiny_todo_v1';
    const todos = JSON.parse(localStorage.getItem(KEY) || '[]');

    function save(){ localStorage.setItem(KEY, JSON.stringify(todos)); render(); }
    function render() {
      listEl.innerHTML = '';
      todos.forEach((t,i) => {
        const li = document.createElement('li');
        li.className = t.done ? 'done' : '';
        li.innerHTML = `<input type="checkbox" ${t.done?'checked':''} data-i="${i}"> ${t.text} <button data-d="${i}">Del</button>`;
        listEl.appendChild(li);
      });
    }
    listEl.addEventListener('click', e => {
      if (e.target.dataset.i !== undefined) {
        const i = +e.target.dataset.i; todos[i].done = e.target.checked; save();
      } else if (e.target.dataset.d !== undefined) {
        todos.splice(+e.target.dataset.d,1); save();
      }
    });
    document.getElementById('add').onclick = () => {
      const v = newEl.value.trim(); if(!v) return;
      todos.push({text:v,done:false}); newEl.value=''; save();
    };
    render();
  </script>
</body>
</html>
