<template>
  <div id="app"> 
    <!--
    <div id="nav" class="text-gray-700 dark:text-white">
      <router-link to="/">Testing</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    -->
    <router-view></router-view>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    opacity:0.5;
    &.router-link-exact-active {
      opacity:1;
    }
  }
}
</style>
