import http from '@/utils/http'

export function readDiscountAPI(params) {
    /* @param page
    *  @param sort_rule */
    return http.get('/steam/discounts', params)
}
