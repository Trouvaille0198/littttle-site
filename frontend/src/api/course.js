import http from '@/utils/http'

export function loginAPI(params) {
    /* @param stuId
    *  @param password
    *  @param termId  */
    return http.post('/course/login', params)
}

export function readCourseRankAPI(params) {
    return http.get('/course/course_rank', params)
}
export function readCourseInfoAPI(params) {
    return http.get('/course/course_info', params)
}
export function readCourseTableAPI(params) {
    return http.get('/course/course_table', params)
}
export function readStuInfoAPI(params) {
    return http.get('/course/stu_info', params)
}