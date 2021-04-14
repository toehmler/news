import Vue from 'vue';
import App from './App.vue';
import router from './router';
import './index.css';

Vue.config.productionTip = false;

Vue.component('news-story', require('./components/Story.vue').default);
//Vue.component('news-article', require('./components/NewsArticle.vue').default);

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
