<template>
    <div class="box mb-4">
        <h3 class="is-size-4 mb-5">Заказ от {{ order.created_at.substr(0, 10) }}</h3>
        <h4 class="is-size-5"> Товары</h4>

        <table class="table is-fullwidth">
            <thead>
                <tr>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Количество</th>
                    <th>Сумма</th>
                </tr>
            </thead>
            <tbody>
                <tr
                    v-for="item in order.items"
                    v-bind:key="item.product.id"
                    >
                    <td>{{ item.product.name }}</td>
                    <td>{{ item.product.price }} руб.</td>
                    <td>{{ item.quantity }}</td>
                    <td>{{ getItemTotal(item).toFixed(2)}} руб.</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                <th scope="row" colspan="3">Общая сумма</th>
                <td colspan="2">{{ getTotalSum(order) }} руб.</td>
                </tr>
            </tfoot>
        </table>
    </div>
</template>
<script>
export default {
    name: 'OrderSummary',
    props:{
        order:Object
    },
    methods:{
        getItemTotal(item){
            console.log(item.product.name)
            return item.quantity * item.product.price
        },
        orderTotalLength(order){
            return order.items.reduce((acc, curVal)=>{
                return acc += curVal.quantity
            }, 0)
        },
        getTotalSum(order){
           return order.items.reduce((c, pr)=>{
                return c += pr.quantity*pr.product.price
            }, 0)
        },
    }
}
</script>
<style scoped>
.box{
    border-radius: 3px;
}

</style>