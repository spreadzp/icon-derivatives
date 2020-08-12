import { Component, OnInit } from '@angular/core';
import { IconProviderService } from 'src/app/services/icon-provider.service';
import { PriceInfo } from 'src/app/interfaces/priceInfo.interface';

@Component({
  selector: 'app-balance',
  templateUrl: './balance.component.html',
  styleUrls: ['./balance.component.scss']
})
export class BalanceComponent implements OnInit {
  result = null;
  lastBlock = null;
  priceInfo = {} as PriceInfo;
  constructor(private iconProviderService: IconProviderService) { }

  ngOnInit(): void {
    this.iconProviderService.getWallet()
      .then(res => this.result = res);
    this.iconProviderService.getLastBlock()
      .then(block => this.lastBlock = block.height);
    this.iconProviderService.getLastPrice()
      .then(newPrice => {
        console.log('newPrice :>> ', newPrice);
        this.priceInfo.price = this.convertHashToInt(newPrice.price) / 10e5;
        this.priceInfo.blockNumber = this.convertHashToInt(newPrice.blockNumber);
      });
  }

  addPrice() {
    this.iconProviderService.setNewPriceAndBlock();
  }

  convertHashToInt(hashValue: string) {
    return parseInt(hashValue, 16);
  }

}
