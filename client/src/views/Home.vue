<template>
  <div class="bg-light">
    <div class="container max-w-screen-xl mx-auto p-3">
   
      <!-- source icons (md viewport and up) -->
      <bias-slider
        :toggle="toggle"
        :initLeftBias="defaultLeft"
        :initRightBias="defaultRight"
        v-on:dragStart="dragStart"
        v-on:dragEnd="fetchArticles"
        v-on:slideEnd="fetchSources">
      </bias-slider>
 
      <!-- source icons (desktop) -->
      <div class="hidden md:flex justify-center my-5">
        <div class="flex mr-5">
          <img 
            v-for="(source, idx) in leftSources" 
            :key="idx" 
            class="w-6 h-6 md:w-9 md:h-9 rounded-xl mx-1" 
            :src="source[3]">
        </div>
        <div class="flex ml-5">
          <img
            v-for="(source, idx) in rightSources" 
            :key="idx" 
            class="w-6 h-6 md:w-9 md:h-9 rounded-xl mx-1" 
            :src="source[3]">
        </div>
      </div>
      <!-- /source icons -->


      <!-- article cards -->

      <!-- small viewports -->
      <div class="md:hidden">
        <mobile-toggle 
          class="mb-5"
          :value="toggle"
          v-on:mobileToggle="toggle = !toggle"
          :leftSources="leftSources" 
          :rightSources="rightSources">
        </mobile-toggle>

        <div v-if="toggle">
          <div v-if="rightArticlesLoading" class="mt-20">
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
          </div>
          <div v-else>
            <news-story v-for="(article, idx) in rightArticles" class="border-4 border-red-800 mb-4" :key="idx" :article="article"></news-story>
          </div>
        </div>
        <div v-else>
          <div v-if="leftArticlesLoading" class="mt-20">
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
          </div>
          <div v-else>
            <news-story v-for="(article, idx) in leftArticles" class="border-4 border-blue-800 mb-4" :key="idx" :article="article"></news-story>
          </div>
        </div>
      </div>
      <!-- / small viewports -->

      <!-- TODO: combine mobile + lg components -->

      <!-- Medium/lg viewports -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-y-3 gap-x-5">
        <div class="hidden md:block">
          <div v-if="leftArticlesLoading" class="mt-20">
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
          </div>
          <div v-else>
            <news-story v-for="(article, idx) in leftArticles" class="border-4 border-blue-800 mb-4" :key="idx" :article="article"></news-story>
          </div>
        </div>
        <div class="hidden md:block">
          <div v-if="rightArticlesLoading" class="mt-20">
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
          </div>
          <div v-else>
            <news-story v-for="(article, idx) in rightArticles" class="border-4 border-red-800 mb-4" :key="idx" :article="article"></news-story>
          </div>
        </div>
      </div>
      <!-- / medium/lg viewports -->

      <!-- /article cards -->

    </div>
  </div>
</template>

<script>
/* eslint-disable */
import 'vue-range-component/dist/vue-range-slider.css'
import VueRangeSlider from 'vue-range-component'

import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'

const axios = require('axios');

export default {
  name: 'Home',
  data() {
    return {
      toggle: true, /* starts to the right */
      leftArticles: [],
      rightArticles: [],
      leftSources: [],
      rightSources: [],
      leftSourcesLoading: true,
      rightSourcesLoading: true,
      leftArticlesLoading: true,
      rightArticlesLoading: true,
      defaultLeft: -50,
      defaultRight: 50

    };
  },
  components: {
    VueRangeSlider,
  },
  methods: {
    dragStart(bias){
      if (bias < 0)
        this.leftArticlesLoading = true;
      else
        this.rightArticlesLoading = true;
    },
    async fetchSources(bias) {
      const query = `https://api.treyoehmler.com/sources?bias=${bias}`;
      if (bias < 0) {
        this.leftSourcesLoading = true;
      } else {
        this.rightSourcesLoading = true;
      }
      return axios.get(query)
        .then((res) => {
          if (bias < 0) {
            this.leftSources = res.data;
            this.leftSourcesLoading = false;
          } else {
            this.rightSources = res.data;
            this.rightSourcesLoading = false;
          }
          return;
        }).catch((err) => {
          console.log(err);
        });

    },
    fetchArticles(bias) {
      if (bias < 0) 
        var sourceList = this.leftSources;
      else
        var sourceList = this.rightSources;
      const query = 'https://api.treyoehmler.com/articles';
//      const query = 'http://localhost:5000/articles';
      axios.post(query, {
          sources: sourceList,
          bias: bias
        })
        .then((res) => {
          if (bias < 0) {
            this.leftArticles = res.data;
            this.leftArticlesLoading = false;
          } else {
            this.rightArticles = res.data;
            this.rightArticlesLoading = false;
          }
          console.log(res.data);
        }).catch((err) => {
          console.log(err);
        });

    },
    async initContent() {
      Promise.all([
        this.fetchSources(this.defaultLeft),
        this.fetchSources(this.defaultRight)
      ]).then(() => {
        this.fetchArticles(this.defaultLeft);
        this.fetchArticles(this.defaultRight);
      })
    }
  },
  mounted() {
    this.initContent();
  },
};
</script>
