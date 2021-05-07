<template>
  <div class="rounded-lg flex flex-col dark:bg-gray-800 lg:flex-row p-2 bg-white shadow-md">
    <div class="flex-none w-100 lg:w-64 h-48 lg:h-auto relative text-left p-2">
      <img :src="article.imageUrl" class="absolute inset-0 w-full h-full object-cover rounded-lg z-0">
      <!--
      <span class="px-2 py-1 text-sm font-semibold text-white bg-red-600 rounded-full z-10 relative top-0 left-0">{{article.source[2]}}</span>
      <span class="ml-3 px-2 py-1 text-sm font-semibold text-white bg-green-600 rounded-full z-10 relative top-0 left-0">{{article.source[2]}}</span>
      -->

        <!--
         <span class="inline-flex items-center justify-center px-2 py-1 text-xs font-bold leading-none text-red-100 bg-red-600 rounded-full">99+</span>
      <p class="dark:text-white relative z-10 text-left sm:hidden">{{article.title}}</p>
      -->
    </div>
    <div class="py-4 px-2 lg:py-2 lg:px-4 text-left flex-auto">
      <div class="flex items-center mb-3">
        <img class="w-5 h-5 rounded-xl" :src="article.source[3]">
        <small class="ml-1 text-gray-800 dark:text-gray-100">{{article.source[0]}}</small>
      </div>
      <h5 class="font-semibold dark:text-white mb-2">{{article.title}}</h5>
      <p v-if="expanded" class="font-light py-2 text-sm dark:text-white">{{article.content}}</p>
      <div class="flex items-center mt-3">
        <p class="text-sm text-gray-800 dark:text-gray-100 mr-4">{{article.date}}</p>
        <a :href="article.url" target="_blank" class="text-gray-800 dark:text-gray-100 flex items-center">
          <span class="font-medium">Read</span>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-6 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
          </svg>
        </a>
        <a @click="expanded=!expanded" class="hover:cursor-pointer text-gray-800 dark:text-gray-100 ml-auto">
          <span v-if="!expanded">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </span>
          <span v-else>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7" />
            </svg>
          </span>
        </a>
      </div>
    </diV>
  </div>
</template>

<script>
export default {
  props: ['article'],
  data() {
    return {
      expanded: false
    }
  },
};
</script>
