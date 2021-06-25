<template>
  <div class="bg-light"> 
    <div class="container max-w-screen-xl mx-auto p-3 justify-center">
      <div class="max-w-4xl text-left mx-auto">

        <h1 class="text-3xl mt-5 font-medium dark:text-white md:text-center">Partisan News Viewer</h1>
        <p class="dark:text-white my-5">This tool aims to create a news feed from sources at different points on the idealogical spectrum. The ratings used to determine these groupings and ordering of bias are pulled from <a href="https://www.adfontesmedia.com/static-mbc/" target="_blank"><u>Ad Fontes Media’s Bias Chart</u></a>. These ratings do not reflect my own beliefs and are the result of work done by the independent group which describes itself as “a public benefit corporation with a mission to make news consumers smarter and news media better”. The full source code for this project can be found on my <a href="https://github.com/toehmler/news" target="_blank"><u>GitHub</u></a>.</p>
        <p class="dark:text-white my-5">Use the range sliders below to adjust the relative strength of idealogical bias for the sources displayed. Move the red slider further right and left slider further left to increase the bias of the sources shown respectively.</p>
        <p class="dark:text-white mb-10 md:hidden">Use the toggle to switch between right and left-leaning sources.</p>

      </div>
   
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
        <mobile-switch
          :toggleState="toggle"
          :leftSources="leftSources"
          :rightSources="rightSources"
          v-on:toggleClick="toggle = !toggle">
        </mobile-switch>
        <!--
        <mobile-toggle 
          class="mb-5"
          :value="toggle"
          v-on:mobileToggle="toggle = !toggle"
          :leftSources="leftSources" 
          :rightSources="rightSources">
        </mobile-toggle>
        -->
        <!--
        <news-story v-for="(article, idx) in rightArticles" class="border-4 border-red-800 mb-4" :key="idx" :article="article"></news-story>
        -->
        
        <div v-if="toggle">
          <div v-if="rightArticlesLoading" class="my-20">
            <p class="small dark:text-white mb-6">Fetching articles...<br>(this may take a few seconds)</p>
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
          </div>
          <news-story v-for="(article, idx) in rightArticles" class="border-4 border-red-800 mb-4" :key="idx" :article="article"></news-story>
        </div>
        <div v-else>
          <div v-if="leftArticlesLoading" class="my-20">
            <p class="small dark:text-white mb-6">Fetching articles...<br>(this may take a few seconds)</p>
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
          </div>
          <news-story v-for="(article, idx) in leftArticles" class="border-4 border-blue-800 mb-4" :key="idx" :article="article"></news-story>
        </div>
      </div>
      <!-- / small viewports -->

      <!-- TODO: combine mobile + lg components -->

      <!-- Medium/lg viewports -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-y-3 gap-x-5 mt-10">
        <div class="hidden md:block">
          <div v-if="leftArticlesLoading" class="my-20">
            <p class="small dark:text-white mb-6">Fetching articles...<br>(this may take a few seconds)</p>
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
          </div>
          <news-story v-for="(article, idx) in leftArticles" class="border-4 border-blue-800 mb-4" :key="idx" :article="article"></news-story>
        </div>
        <div class="hidden md:block">
            <div v-if="rightArticlesLoading" class="my-20">
              <p class="small dark:text-white mb-6">Fetching articles...<br>(this may take a few seconds)</p>
              <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
            </div>
            <news-story v-for="(article, idx) in rightArticles" class="border-4 border-red-800 mb-4" :key="idx" :article="article"></news-story>
        </div>
      </div>
      <!-- / medium/lg viewports -->

      <!-- /article cards -->

    </div>
  </div>
</template>

<script>
/* eslint-disable */
/*
import 'vue-range-component/dist/vue-range-slider.css'
import VueRangeSlider from 'vue-range-component'

import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'
*/

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
      defaultLeft: -64,
      defaultRight: 45, 

    };
  },
  methods: {
    dragStart(bias){
      if (bias < 0)
        this.leftArticlesLoading = true;
      else
        this.rightArticlesLoading = true;
    },
    async fetchSources(bias) {
      const query = `http://localhost:5000/sources?bias=${bias}`;
      if (process.env.VUE_APP_MODE_ENV == 'prod')
        query = `https://api.treyoehmler.com/sources?bias=${bias}`;
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

      const query = 'http://localhost:5000/articles';
      if (process.env.VUE_APP_MODE_ENV == 'prod') 
        query = 'https://api.treyoehmler.com/articles';
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
    console.log(process.env.VUE_APP_MODE_ENV)

  },
};
</script>
