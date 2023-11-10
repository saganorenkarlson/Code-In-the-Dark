
  <template>
    <input class="text_input" :type="type_of_input" :placeholder="placeholder_to_input" :v-model="v_model_input"/> 

  </template>
  
  <script>

export default {
  name: 'text-input',
  props: {
    type_of_input: String,
    placeholder_to_input: String,
    v_model_input: String,
  },
}
  </script>
<style>

.text_input{
  height: 2.4rem;
  width: 70%;
  background-color: #D9D9D9;
  box-shadow: 0px 0px 26px 2px #00897B;
border-radius: 8px;
color: #6a6a6a;
font-family: 'Cascadia Code', sans-serif;
font-size: 1.2rem;
border: 0px;
margin: 10px 0px 10px 0px;
}

.text_input::placeholder{
  color: #969696;

}
</style>