<template>
  <div id="app" class="container">
    <b-navbar toggleable="sm" type="light" variant="light">
      <b-navbar-toggle target="nav-text-collapse"></b-navbar-toggle>

      <b-navbar-brand>Places remember</b-navbar-brand>

      <b-collapse id="nav-text-collapse" is-nav>

      </b-collapse>
      <div class="my-2 my-sm-0">
        <div v-if="isConnected" class="my-2 my-sm-0">
          <b-nav-text>user: {{ name }}</b-nav-text>
        </div>
      </div>
      <div class="ml-2">
        <div v-if="isConnected" class="my-2 my-sm-0">
          <b-button variant="outline" @click="onLogout">Logout</b-button>
        </div>
      </div>
    </b-navbar>
    <div v-if="!isConnected">

      <b-jumbotron header="Places Remember" lead="Here you can store all your best memories, but firstly login using
          Facebook account">
        <facebook-login
          appId="552419792000216"
          @login="onLogin"
          @logout="onLogout"
          @sdk-loaded="sdkLoaded">
        </facebook-login>
      </b-jumbotron>

    </div>
    <router-view></router-view>
  </div>

</template>

<script>
    import facebookLogin from 'facebook-login-vuejs';
    import axios from 'axios';

    export default {
        name: 'App',
        data() {
            return {
                isConnected: localStorage.isConnected || false,
                name: '',
                show: false,
                FB: undefined,
                token: localStorage.token || ''
            }
        },
        components: {facebookLogin},
        methods: {
            sdkLoaded(payload) {
                this.FB = payload.FB
            },
            onLogin() {
                const path = 'https://barakhtaev.engineer/api/facebook/login/';
                const body = {
                    'access_token': 'EAAH2bEF4FNgBAGgnPdwHZCLoRIVroI3FM2RPVLeNYvorpy1Jg6E41qDZBM59r069hgwb12ZCdJlTZBn5jh5y2oV1vL7ZA08angfjihsqbtqaYYkZC6aSTZBkiPmvpqvwGJAN1upTHCELji14KkWFF58jsICeBc9y3HEP7iJZCmBZABYykrxtSP7Vk',
                };
                axios.post(
                    path,
                    body
                ).then((res) => {
                    if (res.status === 200) {
                        this.token = res.data['key'];
                        this.name = res.data['name'];
                        localStorage.isConnected = true;
                        localStorage.token = res.data['key']
                        this.isConnected = true;
                        console.log('test')
                        this.$router.push('/list')
                    }
                })
                    .catch((error) => {
                        console.error(error);
                    });
            },
            onLogout() {
                localStorage.isConnected = false;
                this.isConnected = false;
                this.name = '';
                this.token = '';
                localStorage.token = '';
                this.show = true;
                this.$router.push('/')
            },
        },

        created() {
            const path = 'https://barakhtaev.engineer/api/user/info';
            const headers = {headers: {Authorization: `Token ${localStorage.token}`}}
            axios.get(
                path,
                headers
            ).then((res) => {
                if (res.status === 200) {
                    this.name = res.data['name'];
                    localStorage.isConnected = true
                    this.isConnected = true
                    this.$router.push('/list')
                } else {
                    this.token = '';
                    this.name = '';
                    localStorage.isConnected = false;
                    this.isConnected = false
                }
            })
                .catch((error) => {
                    console.error(error);
                })

        }
    }
</script>

<style>

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;

  }
</style>
