PDE_BASE = 0x220

global mem
mem = []

def init():
	f = file("data.txt")
	for line in f.readlines():
		a = line.strip().split(' ')
		for x in a[2:]:
			mem.append(int(x, 16))
	f.close()

def getcontent(base, index):
	return mem[base + index]

def convert(va):
	print 'Virtual Address 0x%x:' %va
	pde_index = (va >> 10) & 0x1f
	pte_index = (va >> 5) & 0x1f
	offset = va & 0x1f
	pde_content = getcontent(PDE_BASE, pde_index)
	pde_valid = pde_content >> 7
	pt = pde_content & 0x7f

	print '\t--> pde index: 0x%x pde contents: (valid 0x%x, pt 0x%x)' % (pde_index, pde_valid, pt)

	if pde_valid == 0:
		print '\t\t--> Fault (page directory entry not valid)'
		return
	
	pte_base = pt << 5
	pte_content = getcontent(pte_base, pte_index)
	pte_valid = pte_content >> 7
	pfn = pte_content & 0x7f

	print '\t\t--> pte index: 0x%x pte contents: (valid 0x%x, pfn 0x%x)' % (pte_index, pte_valid, pfn)

	if pte_valid == 0:
		print '\t\t\t--> Fault (page table entry not valid)'
		return
	physic_base = pfn << 5
	mem_content = getcontent(physic_base, offset)
	print '\t\t\t--> Translated to Physical Address 0x%x --> Value: 0x%x' % (physic_base + offset, mem_content)

if __name__ == '__main__':
	init()
	f = file('input.txt')
	for line in f.readlines():
		va = int(line.strip().split()[-1], 16)
		convert(va)
		print ''