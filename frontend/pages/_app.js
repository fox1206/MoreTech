import '../styles/globals.css'
import Header from "../layouts/Header";

function MyApp({ Component, pageProps }) {
  return(<Header>
    <Component {...pageProps} />
      </Header>)
}

export default MyApp
