<template>
  <body>
    <div class="search-wrapper">
        <input type="text" placeholder="Search FAQ.." v-model="search_phrase"/>
		<button @click="search">Search</button>
    </div>


    <div >
      <div>

        <md-list v-for="faq in faqs" :key="faq.question">
            <md-list-item class='question' md-expand>
            <span>{{faq.question}}</span>
            <div class='expandable_answer' slot="md-expand" v-html="faq.answer">
            </div>
          </md-list-item>
        </md-list>
      </div>
  </div>

  </body>
</template>

<script>
import Api from "../api.js";

export default {
  name: 'FaqPage',

  data: function() {
    return {
      faqs: [],
      search_phrase: '',
    }
  },

  methods: {
    gotoinfo: function(link){
      this.$router.push(link); 
    },
    search: function(){
        var request_config;
        if(this.$parent.location == ''){
            request_config = {params:{search_phrase: this.search_phrase}};
        }else{
            request_config = {params:{search_phrase: this.search_phrase, district:this.$parent.location}};
        }
        Api.get(`/faqs/filter_faqs/`, request_config)
        .then(response => {
        this.faqs = response.data.faqs;
        }, error => {
        console.error(error);
        });
    }
  },

  mounted(){
    var request_config;
    if(this.$parent.location == ''){
        request_config = {params:{search_phrase: this.search_phrase}};
    }else{
        request_config = {params:{search_phrase: this.search_phrase, district:this.$parent.location}};
    }
    Api.get(`/faqs/get_faqs/`, request_config)
    .then(response => {
      this.faqs = response.data.faqs;
    }, error => {
      console.error(error);
    });
  },


}
</script>

<style lang="scss" scoped>
  $list-width: 100%;

  .full-control {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap-reverse;
  }

  .list {
    width: $list-width;
  }

  .md-list {
    width: 100%;
    max-width: 100%;
    display: inline-block;
  }

  .full-control > .md-list {
    width: $list-width;
    max-width: 100%;
    height: 400px;
    display: inline-block;
    overflow: auto;
    border: 1px solid rgba(#000, .12);
    vertical-align: top;
  }

  .control {
    min-width: 250px;
    display: flex;
    flex-direction: column;
    padding: 16px;
  }

  .md-list-item-text p {
  white-space: normal;
  padding-bottom: 1rem;
}

.question{
  white-space: normal;
  background: grey;
}

.expandable_answer{
  white-space: normal;
  background: lightgray;
}

.search-wrapper {
    position: relative;
    label {
      position: absolute;
      font-size: 12px;
      color: rgba(0,0,0,.50);
      top: 8px;
      left: 12px;
      z-index: -1;
      transition: .15s all ease-in-out;
    }
    input {
      padding: 4px 12px;
      color: rgba(0,0,0,.70);
      border: 1px solid rgba(0,0,0,.12);
      transition: .15s all ease-in-out;
      background: white;
      &:focus {
        outline: none;
        transform: scale(1.05);
        & + label  {
          font-size: 10px;
          transform: translateY(-24px) translateX(-12px);
        }
      }
      &::-webkit-input-placeholder {
          font-size: 12px;
          color: rgba(0,0,0,.50);
          font-weight: 100;
      }
    }
  }

</style>