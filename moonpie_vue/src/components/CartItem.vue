<template>
    <tr >
        <td>{{ item.product.name }}</td>
        <td class="has-text-centered">{{ item.product.price }} руб.</td>
        <td class="has-text-centered">
            <i @click="decrementQuantity(item)" class="fa fa-minus-circle" aria-hidden="true"> </i> 
            {{ item.quantity }} 
            <i @click="incrementQuantity(item)" class="fa fa-plus-circle" aria-hidden="true"> </i>

        </td>
        <td class="has-text-centered">{{ getItemTotal(item).toFixed(2)}} руб. </td>
        <td class="has-text-centered"><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>
<script>


export default {
   name: 'CartItem',
   props:{
       initialItem:Object
   },
   data(){
      return{
          item:this.initialItem
      } 
   },
   methods:{
       getItemTotal(item){
           return item.quantity*item.product.price
       },
       decrementQuantity(item){
           item.quantity-=1
           if (item.quantity===0){
               this.$emit('removeFromCart',item)
           }
           this.updateCart()
       },
        incrementQuantity(item){
           item.quantity+=1
           this.updateCart()
       },
       updateCart(){
           localStorage.setItem('cart',JSON.stringify(this.$store.state.cart))
       },
       removeFromCart(item){
           this.$emit('removeFromCart',item)
           this.updateCart()
       }
   },
}
</script>
<style scoped>

</style>