import http from '@/utils/http'

export function readTodosAPI() {
    return http.get('/todos')
}

export function addTodoAPI(params) {
    return http.post('/todos', params)
}

export function deleteTodoAPI(id) {
    return http.delete(`/todos/${id}`)
}

export function updateTodoAPI(params) {
    return http.put(`/todos/${params.id}`, params)
}