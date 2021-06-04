<template>
  <div>
    <!-- mobile slider -->
    <div class="md:hidden">
      <vue-range-slider 
        ref="mobileSlider"
        :min="currentMin"
        :max="currentMax"
        :bg-style="currentBg"
        :process-style="currentProcess"
        v-model="currentBias"
        @drag-start="$emit('dragStart', currentBias)"
        @drag-end="$emit('dragEnd', currentBias)"
        @slide-end="$emit('slideEnd', currentBias)"
        :clickable="false"
        :tooltip="false">
      </vue-range-slider>
    </div>
    <!-- /mobile slider -->


    <!-- desktop slider -->
    <div class="hidden md:flex flex-row justify-center">
      <div class="w-64">
        <vue-range-slider
          ref="leftSlider"
          :min="-100"
          :max="0"
          :clickable="false"
          :bg-style="leftSliderBg"
          :process-style="processStyle"
          v-model="leftBias"
          @slide-end="$emit('slideEnd', leftBias)"
          @drag-start="$emit('dragStart', leftBias)"
          @drag-end="$emit('dragEnd', leftBias)"
          :tooltip="false">
        </vue-range-slider>
      </div>
      <div class="w-64">

        <vue-range-slider
          ref="rightSlider"
          class="w-64"
          :min="0"
          :max="100"
          :clickable="false"
          :bg-style="processStyle"
          :process-style="rightSliderBg"
          v-model="rightBias"
          @slide-end="$emit('slideEnd', rightBias)"
          @drag-start="$emit('dragStart', rightBias)"
          @drag-end="$emit('dragEnd', rightBias)"
          :tooltip="false">
        </vue-range-slider>
      </div>

    </div>

    <!-- /desktop slider -->

  </div>
    
</template>

<script>
/* eslint-disable */
import 'vue-range-component/dist/vue-range-slider.css'
import VueRangeSlider from 'vue-range-component'

export default {
  props: {
    toggle: {
      type: Boolean,
      required: true
    },
    initLeftBias: {
      type: Number,
      required: true
    },
    initRightBias: {
      type: Number,
      required: true
    },
  },

  data() {
    return {
      leftBias: this.initLeftBias,
      rightBias: this.initRightBias,
    }
  },
  created() {
    this.leftSliderBg = { backgroundColor: 'blue' }
    this.rightSliderBg = { backgroundColor: 'red' }
    this.processStyle = { backgroundColor: 'white' }
  },
  computed: {
    currentMin() { return (this.toggle ? 0 : -100) },
    currentMax() { return (this.toggle ? 100 : 0) },
    currentBg() { return (this.toggle ? this.processStyle : this.leftSliderBg) },
    currentProcess() { return (this.toggle ? this.rightSliderBg : this.processStyle) },
    currentBias: {
      get() { return (this.toggle ? this.rightBias : this.leftBias) },
      set(val) { 
        if (this.toggle) 
          this.rightBias = val;
        else
          this.leftBias = val;
      }
    }
  },
  components: {
    VueRangeSlider
  }

}
</script>
