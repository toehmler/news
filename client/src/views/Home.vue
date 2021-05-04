<template>
  <div class="bg-light">
    <div class="container max-w-screen-xl mx-auto p-3">

    <!-- slider -->
      <div class="flex justify-center flex-row">
        <div class="w-48 md:w-64">
          <vue-range-slider ref="leftSlider" 
                            :min="-100"
                            :max="0"
                            :bg-style="leftSliderBg"
                            :process-style="processStyle"
                            v-model="leftBias"
                            @drag-end="fetchArticles(leftBias)"
                           :tooltip=false>
          </vue-range-slider>
        </div>
        <div class="w-48 md:w-64">
          <vue-range-slider ref="rightSlider" 
                            :min="0"
                            :max="100"
                            :bg-style="processStyle"
                            :process-style="rightSliderBg"
                            v-model="rightBias"
                            @slide-end="fetchArticles(rightBias)"
                           :tooltip=false>

          </vue-range-slider>
        </div>

      </div>
      <!-- /slider -->

      <!-- source icons -->
      <div class="flex justify-center my-5">
        <div class="flex mr-5">
          <img v-for="(source, idx) in leftSources" :key="idx" class="w-6 h-6 md:w-9 md:h-9 rounded-xl mx-1" :src="source[3]">
        </div>
        <div class="flex ml-5">
          <img v-for="(source, idx) in rightSources" :key="idx" class="w-6 h-6 md:w-9 md:h-9 rounded-xl mx-1" :src="source[3]">
        </div>
      </div>
      <!-- /source icons -->

      <!-- article cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-y-3 gap-x-5">
        <div>
          <div v-if="leftLoading" class="mt-20">
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
          </div>
          <div v-else>
            <news-story v-for="(article, idx) in leftArticles" class="border-4 border-blue-800 mb-4" :key="idx" :article="article"></news-story>
          </div>
        </div>
        <div>
          <div v-if="rightLoading" class="mt-20">
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
          </div>
          <div v-else>
            <news-story v-for="(article, idx) in rightArticles" class="border-4 border-red-800 mb-4" :key="idx" :article="article"></news-story>
          </div>
        </div>
      </div>
      <!-- /article cards -->

      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import 'vue-range-component/dist/vue-range-slider.css'
import VueRangeSlider from 'vue-range-component'
const axios = require('axios');

export default {
  name: 'Home',
  data() {
    return {
      leftArticles: [],
      rightArticles: [],
      leftSources: [],
      rightSources: [],
      leftBias: -77,
      rightBias: 68,
      leftLoading: true,
      rightLoading: true,

    };
  },
  created() {
    this.leftSliderBg = {
      backgroundColor: 'blue',
    };
    this.rightSliderBg = {
      backgroundColor: 'red',
    }
    this.processStyle = {
      backgroundColor: 'white',
    };
  },


  components: {
    VueRangeSlider
  },
  methods: {
    fetchArticles(bias) {
      const query = `http://api.treyoehmler.com/api?bias=${bias}`;
      axios.get(query)
        .then((res) => {
          if (bias < 0) {
            this.leftSources = res.data[0];
            this.leftArticles = res.data[1];
            this.leftLoading = false;
          } else {
            this.rightSources = res.data[0];
            this.rightArticles = res.data[1];
            this.rightLoading = false;
          }
          console.log(res.data)
        }).catch((err) => {
          console.log(err);
        });
    },
  },
  mounted() {
    this.fetchArticles(this.leftBias);
    this.fetchArticles(this.rightBias);
  },
};
</script>
