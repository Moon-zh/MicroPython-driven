	#include <reg52.h>
	#define u8 unsigned char
	#define u16 unsigned int
	#define smg P0
	#define e P2
	#define max_green 31
	
	sbit	red_nb=P3^0;
	sbit	yello_nb=P3^1;
	sbit	green_nb=P3^2;
	sbit	red_dx=P3^3;
	sbit	yello_dx=P3^4;
	sbit	green_dx=P3^5;
	sbit	dx_j=P1^0;
	sbit	nb_j=P1^1;
	
	u8 code tab[]={0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90,0x88,0x83,0xc6,0xa1,0x86,0x8e};
	
	u8 led_nb,led_dx,ds[4],jsbz,cxbz,bz;
	
	void	delay(unsigned long a)
	{
		while(a--);
	}
	
	void	dxtx()
	{
		green_dx=1;
		red_dx=0;
		yello_dx=0;
		
		green_nb=0;
		red_nb=1;
		yello_nb=0;
	}
	
	void	nbtx()
	{
		green_dx=0;
		red_dx=1;
		yello_dx=0;
		
		green_nb=1;
		red_nb=0;
		yello_nb=0;
	}
	
	void	dxh()
	{
		green_dx=0;
		red_dx=0;
		yello_dx=1;
	}
	
	void	nbh()
	{
		green_nb=0;
		red_nb=0;
		yello_nb=1;
	}
	
	void	smxs()
	{
		u8 i=0;
		ds[0]=led_nb/10;
		ds[1]=led_nb%10;
		ds[2]=led_dx/10;
		ds[3]=led_dx%10;
		for(P2=1;P2!=0x10;P2<<=1)
		{
			smg=tab[ds[i++]];
			delay(20);
			smg=0xff;
		}
	}
	
	void	zdsz()
	{
		TMOD=0X11;
		TH0=0X3C;
		TL0=0XB0;
		ET0=TR0=ET1=TR1=EA=1;
	}
	
	void	init()
	{
		led_dx=max_green;
		led_nb=max_green+3;
		jsbz=0;
		cxbz=0;
	}
	
	void	main()
	{
		init();
		zdsz();
		while(1)
		{
			switch(cxbz)
			{
				case 0:
						dxtx();break;
				case 1:
						dxh();break;
				case 2:
						nbtx();break;
				case 3:
						nbh();break;
				case 4:
						init();
			}
			smxs();
		}
	}
	
	void	zd() interrupt 1
	{
		TH0=0X3C;
		TL0=0XB0;
		
		if(++jsbz==20)
		{
			jsbz=0;
			if(--led_dx==0)
			{
				if(cxbz==0)led_dx=3,cxbz++;
				else if(cxbz==1)led_dx=max_green+3,led_nb=max_green,cxbz++;
				else led_dx=max_green,cxbz=0;
			}
			if(--led_nb==0)
			{
				if(cxbz==2)led_nb=3,cxbz++;
				else if(cxbz==3)led_nb=max_green+3,led_dx=max_green,cxbz=0;
				else led_nb=max_green,cxbz=0;
			}
		}
	}
	
	void	zd_j() interrupt 3
	{
		if(!dx_j)
		{
			TR0=0,smg=0xff;
			dxtx();
			while(!dx_j);
			TR0=1;
		}
		if(!nb_j)
		{
			TR0=0,smg=0xff;
			nbtx();
			while(!nb_j);
			TR0=1;
		}
	}