import { Injectable } from '@angular/core';
// import { IconService, HttpProvider, IconWallet } from 'icon-sdk-js';
import IconService, { HttpProvider, IconWallet} from 'icon-sdk-js';
@Injectable({
  providedIn: 'root'
})
export class IconProviderService {
  provider = null;

  /* Create IconService instance */
  // iconService = null;
  async getWallet() {
    // this.provider = new HttpProvider('https://bicon.net.solidwallet.io/api/v3');
    // console.log('this.provider :>> ', this.provider);
    // const iconService = new IconService(this.provider);
    //
    const ks = { 'version': 3, 'id': '38bc33f5-4873-4386-9188-043bb6897bf9', 'address': 'hx961cb5b5859ece30c472312182d12b4c01b8f103', 'crypto': { 'ciphertext': '2d670add77faa900605d300197b7215375c9029b86b59f959582f44fcce9da70', 'cipherparams': { 'iv': '0b6c82cf3ef081e108a250fe919f090b' }, 'cipher': 'aes-128-ctr', 'kdf': 'scrypt', 'kdfparams': { 'dklen': 32, 'salt': 'ef2b2dcc1ff4acf2eec5d01467689b01feb2797e30e59747a66ab83606f31ac1', 'n': 16384, 'r': 8, 'p': 1 }, 'mac': '2004b80ec680981ab331c322aca6b053b66951ea4192c751c170aa292308acf9' }, 'coinType': 'icx' };
    const pw = '12345678_Liza';

    // console.log('wallet :>> ', wallet);
    // let wallet = IconWallet.create(); // Wallet Creation
    // const address = wallet.getAddress(); // Get Address
    // const privateKey = wallet.getPrivateKey(); //  Get Private Key
    // wallet = IconWallet.loadPrivateKey(privateKey);
    // return JSON.stringify(wallet);
    // const iconService = new IconService(new HttpProvider('https://bicon.net.solidwallet.io/api/v3'));
    // console.log('iconService :>> ', iconService);
    // const { IconWallet } = iconService;
    // const wallet = IconWallet.create();
    const iconService = await new IconService(new HttpProvider("https://bicon.net.solidwallet.io/api/v3"));
    console.log('iconService :>> ', iconService);
    const { CallBuilder } = IconService.IconBuilder;
    const wallet = IconWallet.create();
    console.log(wallet.getAddress());
    const callObj = new CallBuilder()
    .to('cx09a47e15ee131726db1f5639a22b86c05a3b17b2')
    .method('hello')
    .build();

/* Executes a call method to call a read-only API method on the SCORE immediately without creating a transaction on Loopchain */
    const result =  iconService.call(callObj).execute();
    // const wallet = IconWallet.loadKeystore(ks, pw);

    console.log('result :>> ', result.toString());
    return  result;
  }
}
