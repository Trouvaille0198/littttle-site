import { readTodosAPI, addTodoAPI, deleteTodoAPI, updateTodoAPI } from '@/api/todo'
const state = {

    todos: []
}

const getters = {
    doneTodos: state => {
        return state.todos.filter(todo => todo.is_done)
    },
    doneTodosNum: (state, getters) => {
        return getters.doneTodos.length
    },
    getTodoById: state => id => {
        return state.todos.find(todo => todo.id === id)
    }
}

const mutations = {
    // 在同步方法中对静态页面进行内容的"假"更新
    // readTodos(state) {
    //     readTodosAPI().then(
    //         res => { state.todos = res; }
    //     )
    // },
    addTodo(state, todo) {
        state.todos.push(todo);
        state.newTodoTitle = "";
    },
    shiftTodo(state, id) {
        let todo = state.todos.filter((todo) => todo.id === id)[0];
        todo.is_done = !todo.is_done;
        todo.is_done = !todo.is_done;
    },
    deleteTodo(state, id) {
        state.todos = state.todos.filter((todo) => todo.id !== id);
    },
}

const actions = {
    // 在异步方法中真正实现与后端的数据交换
    readTodos() {
        // context.commit('readTodos');
        readTodosAPI().then(
            res => { state.todos = res; }
        )
    },
    addTodo(context, newTodo) {
        addTodoAPI(newTodo).then(
            res => {
                // 用后端返回的数据做页面的更新
                context.commit('addTodo', res);
            }
        )
    },
    deleteTodo(context, id) {
        deleteTodoAPI(id).then(
            res => {
                context.commit('deleteTodo', res.id);
            }
        )
    },
    shiftTodo(context, id) {
        let shiftedTodo = state.todos.filter((todo) => todo.id === id)[0];
        shiftedTodo.is_done = !shiftedTodo.is_done
        updateTodoAPI(shiftedTodo).then(
            res => {
                context.commit('shiftTodo', res.id);
            }
        )
    }
}
export default {
    state,
    getters,
    mutations,
    actions
}