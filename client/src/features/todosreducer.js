import { createSlice } from "@reduxjs/toolkit";

const todosSlice = createSlice({
    name: "todos",
    initialState:[],
    reducers:{
        getTodos(state){
            const fetchData=async ()=>await fetch("http://127.0.0.1:8000/api/todo")
            .then(async (res) => await res.json())
            .then((todos_list) => {
                state=todos_list;
                // console.log(state);
            });
            fetchData();
        }
    }
});

export const {getTodos} = todosSlice.actions;
export default todosSlice.reducer;