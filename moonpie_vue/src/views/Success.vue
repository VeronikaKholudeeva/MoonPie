<template>
 <div class="my-page">
    <div class="blur-wrapper">
    <div class="hero is-fullheight page-success ">
        <div class="column is-multiline success">
            <div class="column is-12 has-text-centered">
                <img class="car" src="../assets/pic/success.png">
                <h1 class="is-size-2"> Спасибо </h1>
                <p> Ваш заказ успешно принят, он появится в личном кабинете в ближайшее время!</p>
            </div>
        </div>
    </div>
    </div>
 </div>
</template>

<script>


export default {
    name: 'Success',
    mounted(){
        document.title = 'Success | MoonPie'
    },
}
</script>
<style scoped>
.page-success{
    font-family:'Gotham Pro';
    padding-top:80px;
}
.success{
    padding: 50px;
    padding-top: 30px;
    background-color: rgb(255, 247, 242);
}
h1{
    margin-top:50px;
}
img{
    height: 150px;
    width: 150px;
    margin-top:10%;
}
</style>