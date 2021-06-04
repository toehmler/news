<template>
  <div class="mt-5"> 
    <span
      class="toggle-wrapper"
      @click="toggle">
      <span
        class="toggle-background"
        :class="backgroundStyles">
        <div class="flex items-center justify-center" style="height:38px">
          <img
            v-if="!value"
            v-for="(source, idx) in leftSources"
            :key="idx"
            class="w-7 h-7 rounded-xl mx-1"
            :src="source[3]">
          <img 
            v-if="value"
            v-for="(source, idx) in rightSources"
            :key="idx"
            class="w-7 h-7 rounded-xl mx-1"
            :src="source[3]">
        </div>
      </span>
      <span 
        class="toggle-indicator"
        :style="indicatorStyles"/>
    </span>
  </div>
</template>

<script>
export default {
  props: {
    leftSources: {
      type: Array,
      required: true,
    },
    rightSources: {
      type: Array,
      required: true,
    },
    value: {
      type: Boolean,
      required: true
    }
  },
  computed: {
    backgroundStyles() {
      return {
        'gold-mid': this.value,
        'gray-lighter': !this.value
      };
    },
    indicatorStyles() {
      return { transform: this.value ? 'translateX(254px)' : 'translateX(0)' };
    }
  },
  methods: {
    toggle() {
      this.$emit('mobileToggle');
    }
  }
};
</script>
<style scoped>
.gold-mid{
  background-color: rgba(255, 0, 0, 0.3);
}

.gray-lighter{
  background-color: rgba(0,0,255,0.3);
}

.toggle-wrapper {
  display: inline-block;
  position: relative;
  cursor: pointer;
  width: 292px;
  height: 38px;
  border-radius: 9999px;
  user-select:none;
}

.toggle-wrapper:focus {
  outline: 0;
}

.toggle-background {
  display: inline-block;
  border-radius: 9999px;
  height: 100%;
  width: 100%;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: background-color .4s ease;
}

.toggle-indicator {
  position: absolute;
  height: 34px;
  width: 34px;
  left: 2px;
  bottom: 2px;
  background-color: #ffffff;
  border-radius: 9999px;
  box-shadow:  0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform .4s ease;
}
</style>




