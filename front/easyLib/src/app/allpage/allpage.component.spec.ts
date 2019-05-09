import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AllpageComponent } from './allpage.component';

describe('AllpageComponent', () => {
  let component: AllpageComponent;
  let fixture: ComponentFixture<AllpageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AllpageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AllpageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
