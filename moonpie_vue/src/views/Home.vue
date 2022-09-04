<template>
  <div class="home">
    <section class="hero is-fullheight mb-6">
      <div class="hero-body has-text-centered">
        <p class="title is-1 mb-6">
          Добро пожаловать на сайт кондитерской MoonPie
        </p>
        <p class="subtitle is-6">
          Кондитерская "Moon Pie" работает с 2015 года, и на сегодняшний день мы обслужили более чем 1000 клиентов.
            Умелые и талантливые мастера нашей кондитерской трудятся с любовью и отдачей над приготовлением истинных шедевров кулинарии.
        </p>
      </div>
    </section>
    <div class="content-home">
      
      <div class="columns is-multiline is-vcentered">
        <div class="column is-12">
          <p class="is-size-2 has-text-centered">Хиты продаж</p>
        </div>
      </div> 
       <div class="products column is-12">
            <div class="columns is-multiline">   
            <ProductBox
                v-for="product in products"
                v-bind:key="product.id"
                v-bind:product="product"/>
            </div>
       </div>
      <div class="columns is-multiline is-vcentered rew">
        
            <div class="column is-12">
              <p class="is-size-2 has-text-centered">Что о нас говорят люди</p>
            </div>
            <div class="more is-medium">
              <router-link to="/review" class=" navbar-item has-text-centered" >Прочитайте больше</router-link>
            </div>
            
            <div class="columns is-multiline is-mobile rev ">
              <Reviews 
                      v-for="review in getReview"
                      v-bind:key="review.id"
                      v-bind:review="review"/>
            </div>    
        
      </div>
      <div class="columns is-multiline is-vcentered delivery">
        <div class="column is-12">
          <p class="is-size-2 has-text-centered">Информация о доставке</p>
        </div>
        <div class="column is-12 delivery-info">
          <p class="is-size-4 has-text-centered">Условия доставки по городу Краснодар и Краснодарскому краю</p>
          <p class="is-size-6 has-text-centered">По городу Краснодар бесплатная доставка осуществляется при заказе на сумму от 5000 рублей.</p>
          <p class="is-size-6 has-text-centered">При заказе на сумму менее 5000 рублей доставка рассчитывается менеджером по тарифам такси. 
            Стоимость доставки напрямую зависит от дальности расстояния доставки. Доставка осуществляется в часовом интервале с 9:00 до 18:00. 
            Доставка после 18:00 возможна после индивидуального согласования.</p>
          <p class="is-size-6 has-text-centered">При оформлении заказа обязательно укажите правильные контактные данные (имя, телефон, e-mail), дату доставки и интервал. 
            При необходимости, менеджер свяжется с вами и согласует время и дату доставки вашего заказа. 
            Заказы с безналичным способом оплаты должны быть оплачены накануне дня доставки до 18:00 по будням и до 16:00 в выходные и праздничные дни.</p> 
          <p class="is-size-6 has-text-centered">Доставка по Краснодарскому краю осуществляется в специально машине холодильнике, стоимость доставки рассчитывается индивидуально и напрямую зависит от дальности доставки.</p>
          <p class="is-size-6 has-text-centered"><b>Самовывоз по адресу:</b> г. Краснодар, ул. Кореновская 38.</p>
          <p class="is-size-6 has-text-centered"><b>Телефон:</b> 8 (999) 666 99 66</p> 
          <p class="is-size-6 has-text-centered"><b>Забрать заказанную продукцию вы можете ежедневно с 9:00 до 18:00.</b></p>
          <img class="car" src="../assets/pic/delivery.png">
          
        </div>
      </div>
      <div class="columns is-multiline is-vcentered faq">
        
        <div class="faq-box">
          <div class="column is-12">
          <p class="is-size-2 has-text-centered">Часто задаваемые вопросы</p>
        </div>
            
            <h3 class="is-size-5"><i class="fas  fa-question-circle"></i> Как оформить заказ на вашем сайте?</h3>
            <p class="is-size-6 has-text-grey">1. Зарегистрируйтесь на сайте или войдите в свою учетную запись. Если вам понравился торт, добавьте его в корзину. Перейдите в корзину и нажмите кнопку «Оформить заказ». В течение 5 минут мы вам перезвоним и согласуем заказ.</p>
            <p class="is-size-6 has-text-grey">2. Позвоните по телефону 8 (999) 666-99-66 или напишите в WhatsApp и оформите заказ вместе с оператором.</p>
            
            <h3 class="is-size-5"><i class="fas  fa-question-circle"></i> За какое время лучше сделать заказ торта?</h3>
            <p class="is-size-6 has-text-grey">Оптимальное время для заказа небольших тортиков или десертов за 3 дня. Свадебные торты лучше заказывать за неделю. Но мы всегда готовы принять и срочные заказы. </p>
            
            <h3 class="is-size-5"><i class="fas  fa-question-circle"></i> Из каких ингредиентов вы делаете торты?</h3>
            <p class="is-size-6 has-text-grey">Мы готовим торты и десерты из натуральных ингредиентов, а именно: из яиц категории С1, пшеничной муки высшего сорта, натурального сливочного масла, творожного сыра и сливок. Сами готовим джемы. Вы можете быть уверены в натуральности и качестве используемых ингредиентов. </p>
          
            <h3 class="is-size-5"><i class="fas  fa-question-circle"></i> Как можно отменить заказ?</h3>
            <p class="is-size-6 has-text-grey">Если вы передумали или у вас изменились планы вы можете отменить заказ за 3 дня до планируемой даты, в таком случае мы вернем вам всю оплаченную сумму. Если вы отмените заказ менее чем за 3 дня оплаченная сумма не возвращается. </p>
         
            <h3 class="is-size-5"><i class="fas  fa-question-circle"></i> Есть ли у вас доставка, сколько стоит?</h3>
            <p class="is-size-6 has-text-grey">У нас есть бесплатная доставка по городу Краснодар при заказе на сумму 5 000 руб. При заказе на сумму меньше доставка платная, стоимость от 150 руб. Рассчитывается доставка исходя из вашего точного местоположения. Стоимость можно уточнить у менеджера при оформлении заказа.</p>
         
            <h3 class="is-size-5"><i class="fas  fa-question-circle"></i> Существует ли возможность самовывоза?</h3>
            <p class="is-size-6 has-text-grey">Ежедневно с 09:00 до 18:00 вы можете бесплатно забрать десерт на производстве по адресу г. Краснодар, ул. Кореновская 1. Если вы хотите забрать заказ раньше или позже указанного времени сообщите нам об этом при оформлении заказа.</p>
          
            <h3 class="is-size-5"><i class="fas  fa-question-circle"></i> Что делать, если получатель торта не я?</h3>
            <p class="is-size-6 has-text-grey">Мы очень любим доставлять торты-сюрпризы! Вам нужно оплатить 100% стоимости торта вместе с доставкой, а получателю мы сможем передать ваше поздравление.</p>
        
            <h3 class="is-size-5"><i class="fas  fa-question-circle"></i> Упакованы ли ваши десерты и как?</h3>
            <p class="is-size-6 has-text-grey">Каждый наш торт или десерт упакован в специальную брендированную коробку, которая идеально подходит для транспортировки и для подарка. Упаковка входит  в стоимость десерта.</p>
         
        </div> 
      </div>
      <div class="columns is-multiline kontakt">
        <div class="column is-12">
        <h1 class="is-size-2 has-text-centered">Контактная информация</h1>
        </div>
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d704.0832210818882!2d38.973754765256004!3d45.09931962226456!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40f0467e3cc80e1d%3A0x1ebdd611c2dc1611!2z0YPQuy4g0JrQvtGA0LXQvdC-0LLRgdC60LDRjywgMzgsINCa0YDQsNGB0L3QvtC00LDRgCwg0JrRgNCw0YHQvdC-0LTQsNGA0YHQutC40Lkg0LrRgNCw0LksIDM1MDAwNQ!5e0!3m2!1sru!2sru!4v1653343144031!5m2!1sru!2sru" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        <div class="kon">
        <p><i class="fa fa-map-marker" aria-hidden="true"></i> г. Краснодар, ул. Кореновская, 38</p>
        <p><i class="fa fa-phone mt-4" aria-hidden="true"></i> 9 (999) 666 99 66</p>
        <p><i class="fa fa-envelope mt-4" aria-hidden="true"></i> moonpie@mail.ru</p>
        <p><i class="fa fa-clock mt-4" aria-hidden="true"></i> Ежедневно с 9.00 до 22.00</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Reviews from '@/components/Reviews.vue'
import ProductBox from '@/components/ProductBox.vue'
import Flickity from 'vue-flickity';


export default {
  name: 'Home',
  data(){
    return{
      getReview: [],
      products:[],
      
    }
  },
  components: {
    Reviews,
    ProductBox,
  },
  mounted(){
    this.getReviews()
    this.gethotProducts()
    document.title = 'Home | MoonPie'

  },
  methods:{
    gethotProducts(){
      axios
        .get('/api/v1/gethotProduct/')
        .then(response =>{
          this.products = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    getReviews(){
      axios
        .get('/api/v1/getLastReview/')
        .then(response =>{
          this.getReview = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    
  }
}
</script>


<style scoped>

section{
  padding: 0,0,0,0;
  
}
.faq{
  padding:50px;
}
.faq-box h3{
  padding-top:20px;
  padding-bottom: 10px;;
  font-weight: bold;
}
.faq-box{
 font-family: 'Gotham Pro';
 padding:50px;
}
.faq-box{
 box-shadow: rgba(0, 0, 0, 0.45) 10px 15px 10px -10px;
 margin:10px 0;
  border-radius: 7px;
  border: 1pt solid rgba(253, 249, 244, 0.4);
 background-color: rgba(255, 255, 255, 1);
 
}
.faq-box p{
  padding-left:20px;
}
.fas{
  font-weight: normal;
}
.kontakt{
  font-family: 'Gotham Pro';
  padding:50px;
}
i{
  font-size: 20px;
  
}

.kon{
  padding: 50px;
}
iframe{
  padding-top:20px;
}
.car{
  padding-left: 35%;
  
}
.car:hover{
  padding-left:50%;
  transition: padding-left 2s;
}

.delivery-info{
  font-family: 'Gotham Pro';
}
.delivery{
  padding: 100px;
  padding-bottom: 0px;
}
.delivery p{
  padding-top: 10px;
}
.more{
  text-align: center;
  margin: auto;
}
.more .navbar-item{
  color: #1C0800;
  border-bottom: 2pt solid rgb(28,8,0, 0.1);

}
.more .navbar-item:hover{
  color:rgb(28,8,0);
  background-color: rgb(28,8,0, 0.1);
}
.rev{
  padding: 30px;

}
.rew{
  padding-top: 100px;
  margin: auto;
  
}
.review-container{
 
  padding: 60px;
}
.home{
font-family:'Gotham Pro';
background-color: rgb(255, 247, 242);
}
.hero{
  background-image: url("../assets/pic/background.jpg");
}
.content-home p{
  font-weight: lighter;
  letter-spacing: 3px;
}
img{
  height: 450px;
}
.subtitle{
  text-align: center;
  color: rgb(201, 187, 170);
  font-weight:normal;
  
}
.title{
  color: antiquewhite;
  font-weight: lighter;
  letter-spacing: 5px;
}
.hero-body{
  background-color: rgba(10, 5, 0, 0.7);
  backdrop-filter: blur(5px);
  flex-direction: column;
  justify-content: center;
  
}
.box{
  width: 340px;
  margin: 0 10px;
  border-radius: 0px;
  box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
}
</style>

