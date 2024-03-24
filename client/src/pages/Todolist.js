import { useSelector } from 'react-redux';
import { useDispatch } from 'react-redux';
import { getTodos } from '../features/todosreducer';

export default function Todolist() {
    const todos = useSelector((state) => state.data);
    const dispatch = useDispatch();
    return (
            console.log(todos),
        <div>
            {todos.map(todo => (
                <div key={todo.id}>
                    {/* <h3>Title: {todo.title} + Description: {todo.description}</h3> */}
                    console.log(todo)
            </div>
            ))}
            <button onClick={()=>dispatch(getTodos())} >Refresh</button>
        </div>
    );
}
